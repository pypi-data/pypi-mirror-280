# order_manager.py
import datetime
import uuid
from turtle import pensize
from typing import List, Tuple

import pendulum
from galapy_core.oms.database_manager import (
    DatabaseManager,
    SupabaseDatabaseManager,
)
from galapy_core.oms.exchange_api import ExchangeAPI, MockExchangeAPI
from galapy_core.portfolio import get_portfolio_with_assets
from loguru import logger
from supabase import AClient
from supamodel import supabase_client as supabase
from supamodel.enums import OrderSide, OrderStatus, PositionStatus
from supamodel.trading.order_management import Order, Trade
from supamodel.trading.portfolio import Position

# AClient(supabase_url=, supabase_key="")


# TODO: I EVENTUALLY WANT TO GRAB EXCHANGE API BY ID or Name ONLY. That information is easily accessible to the user and portfolio owner.
#
class OrderHandler:
    def __init__(self, exchange_api: ExchangeAPI, db_manager: DatabaseManager):
        self.exchange = exchange_api
        self.database = db_manager

    def submit_order(self, order: Order) -> Order:
        # Submit the order to the exchange
        exchange_order = self.exchange.submit_order(order)

        # Save the order to the database
        saved_order = self.database.save_order(exchange_order)

        return saved_order

    def update_order_status(self, order_id: str, status: OrderStatus) -> Order:
        # Update the order status in the database
        if isinstance(status, str):
            status = OrderStatus(status)
        updated_order = self.database.change_order_status(order_id, status)

        return updated_order

    def process_order(self, order: Order) -> Trade:
        # Create or update the position based on the order
        position = self.database.create_position(order)

        # Create a trade record
        trade = Trade(
            position_id=position.id,
            order_id=order.id,
            quantity=order.quantity,
            price=order.price,
            fee=self.exchange.calculate_fee(order),
            timestamp=self.exchange.get_fill_timestamp(order),
        )

        # Save the trade to the database
        saved_trade = self.database.save_trade(trade)

        return saved_trade

    def get_trade_by_id(self, trade_id: uuid.UUID | str) -> Trade:
        result = supabase.table("trades").select("*").eq("id", str(trade_id)).execute()
        if result.data and len(result.data) > 0:
            return Trade(**result.data[0])
        else:
            raise ValueError(f"No trade found with id {trade_id}")

    # Figure out how to reduce the number of calls to the database
    def update_position(self, order: Order, trade: Trade) -> Position:
        # # Retrieve the position from the database
        position = self.database.get_position(trade.position_id)

        # Retrieve the portfolio from the database
        portfolio = self.database.get_portfolio(position.portfolio_id)

        # Update the position based on the order and trade details
        fill_quantity, fill_price = self.exchange.get_fill_details(order)
        if order.side == OrderSide.BUY:
            position.quantity += fill_quantity
            position.average_price = fill_price

            # Update the portfolio balance
            portfolio.balance -= fill_quantity * fill_price

            # Set the opened_by trade if the position is being opened
            if position.opened_trade is None:
                position.opened_at = trade.timestamp
                position.opened_trade = trade.id
        else:
            if fill_quantity > position.quantity:
                # Update position to 0 if the sell quantity exceeds the position quantity
                # This can happen if the position is closed manually or by a stop loss order
                position.quantity = 0
                position.closed_at = trade.timestamp
                position.closed_trade = trade.id
                position.status = PositionStatus.CLOSE

            else:
                position.quantity -= fill_quantity

                # Update the portfolio balance
                portfolio.balance += fill_quantity * fill_price

                # Set the closed_by trade if the position is being closed
                if position.quantity == 0:
                    position.closed_at = trade.timestamp
                    position.closed_trade = trade.id
                    position.status = PositionStatus.CLOSE

        # Save the updated position to the database
        _ = self.database.save_position(position)

        # Save the updated portfolio to the database
        return self.database.save_portfolio(portfolio)

        # return updated_position

    def check_open_orders(self) -> None:
        # Retrieve open orders from the database
        open_orders = self.database.get_open_orders_from_db()

        for order in open_orders:
            # Retrieve the order from the exchange
            self.handle_order_status(order)

    def handle_order_status(self, order: Order) -> Order | None:
        def get_order(order_id) -> Order:
            return Order(
                **(
                    supabase.table("orders")
                    .select("*")
                    .eq("id", str(order_id))
                    .execute()
                ).data[0]
            )

        self.exchange.get_order = get_order
        exchange_order = self.exchange.get_order(order.id)

        # Check the order status
        if exchange_order.status in [
            OrderStatus.FILLED,
            OrderStatus.PARTIALLY_FILLED,
        ]:
            # Process the order and update the position
            trade = self.process_order(exchange_order)
            self.update_position(exchange_order, trade)
            self.update_order_status(order.id, exchange_order.status)
        elif exchange_order.status == OrderStatus.CANCELED:
            # Update the order status in the database
            self.update_order_status(order.id, exchange_order.status)
        elif exchange_order.status == OrderStatus.REJECTED:
            # Update the order status in the database
            self.update_order_status(order.id, exchange_order.status)
