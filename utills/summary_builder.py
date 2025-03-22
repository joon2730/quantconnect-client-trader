def summarize_portfolio(portfolio):
    summary = {
        "total_cash": portfolio.cash,
        "portfolio_value": portfolio.total_portfolio_value,
        "unrealized_profit": portfolio.total_unrealised_profit,
        "holdings": {}
    }

    for symbol, holding in portfolio.items():
        if holding.Invested:
            summary["holdings"][str(symbol)] = {
                "quantity": str(holding.quantity),
                "avg_price": holding.average_price,
                "holdings_value": holding.holdings_value,
                "unrealized_profit": holding.unrealized_profit,
            }

    return summary

def summarize_order_event(order_event):
    summary = {
        "order_id": order_event.order_id,
        "symbol": str(order_event.symbol),
        "status": str(order_event.status).lower(),
        "direction": str(order_event.direction).lower() if order_event.direction else None,
        "fill_quantity": order_event.fill_quantity,
        "fill_price": order_event.fill_price if order_event.fill_quantity != 0 else None,
        "message": order_event.message or "",
        "order_fee": float(order_event.order_fee.value.amount) if order_event.order_fee else 0
    }

    return summary