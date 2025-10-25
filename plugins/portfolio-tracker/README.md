# Investment Portfolio Tracker Plugin

Investment portfolio monitoring and analysis specialist with real-time pricing and performance insights.

## Overview

Track your complete investment portfolio across all asset classes with real-time price updates, performance analysis, rebalancing recommendations, and tax-loss harvesting opportunities.

## Agent

### portfolio-analyzer (Sonnet)
**Description**: PROACTIVELY monitors investment portfolios with real-time pricing

**Capabilities**:
- Multi-asset tracking (stocks, bonds, crypto, real estate)
- Real-time price updates via financial APIs
- Portfolio performance (ROI, IRR, time-weighted returns)
- Asset allocation visualization and analysis
- Rebalancing recommendations with specific trades
- Tax-loss harvesting opportunity identification
- Dividend and interest income tracking

**Use When**:
- Adding new investments
- Checking current portfolio value
- Analyzing performance and returns
- Getting rebalancing advice
- Finding tax-loss harvesting opportunities
- Tracking dividend income

**Tools**: Read, Write, Bash, WebFetch

## Features

✅ **Multi-Asset Support**: Stocks, bonds, crypto, real estate, commodities
✅ **Real-Time Pricing**: Yahoo Finance, CoinGecko, Alpha Vantage
✅ **Performance Analytics**: ROI, IRR, time-weighted returns
✅ **Smart Rebalancing**: Automated recommendations based on targets
✅ **Tax Optimization**: Tax-loss harvesting with wash sale awareness
✅ **Income Tracking**: Dividends, interest, rental income
✅ **Asset Allocation**: Visual breakdown with target comparison

## Usage Examples

### Add New Investment

```
Use portfolio-analyzer to add my Apple stock purchase:
- Ticker: AAPL
- Quantity: 10 shares
- Purchase price: $150/share
- Date: Jan 15, 2024
- Account: Vanguard Brokerage
```

**Result**: Investment added and current price fetched

### Check Portfolio Value

```
Use portfolio-analyzer to show my current portfolio value
```

**Result**:
```
📊 Portfolio Summary (as of Nov 18, 2025)

Total Value: $125,450.00
Total Cost Basis: $110,000.00
Total Return: +$15,450.00 (+14.0%)

By Asset Type:
Stocks        $75,270 (60.0%) ✅ On target
Bonds         $25,090 (20.0%) ✅ On target
Crypto        $13,400 (10.7%) ⚠️ Slightly over
Real Estate   $11,690 (9.3%)  ⚠️ Slightly under
```

### Get Rebalancing Advice

```
Use portfolio-analyzer to recommend rebalancing trades
```

**Result**:
```
🔄 Rebalancing Recommendations

Portfolio is 7.3% out of target allocation.

1. SELL $2,500 of Crypto (10.7% → 10.0%)
   Sell 0.037 BTC at $67,000

2. BUY $2,500 of Real Estate
   Consider VNQ (Vanguard REIT ETF)

After rebalancing, all allocations on target.
```

### Find Tax-Loss Harvesting

```
Use portfolio-analyzer to identify tax-loss harvesting opportunities
```

**Result**:
```
💰 Tax-Loss Harvesting Opportunities

You can realize $3,450 in capital losses:

1. AGG (Bond ETF) - $1,500 loss (-13.6%)
   Purchased: Mar 1, 2024
   Strategy: Sell and buy BND (similar bond ETF)

2. INTC (Intel) - $1,950 loss (-28.8%)
   Purchased: Jul 15, 2024
   Strategy: Sell and wait 31 days or buy AMD

Total tax benefit: ~$830 (24% bracket)
```

## Supported Asset Types

| Asset Type | Examples | Price Source |
|------------|----------|--------------|
| **Stocks** | AAPL, TSLA, VTI | Yahoo Finance |
| **Bonds** | AGG, BND, TLT | Yahoo Finance |
| **Crypto** | BTC, ETH, SOL | CoinGecko |
| **Real Estate** | REITs, rental properties | Yahoo Finance / Manual |
| **Cash** | Savings, CDs, money market | Manual |
| **Commodities** | Gold, silver ETFs | Yahoo Finance |

## Financial APIs

### Yahoo Finance (Primary)
- **Stocks and ETFs**: Real-time quotes
- **Free**: No API key needed
- **Coverage**: US and international markets
- **Rate Limit**: Generally permissive

### CoinGecko (Crypto)
- **Cryptocurrencies**: BTC, ETH, and 10,000+ coins
- **Free tier**: 50 requests/minute
- **No API key**: For basic usage
- **Global pricing**: Multiple currencies

### Alpha Vantage (Alternative)
- **Free tier**: 25 requests/day
- **Requires**: API key (free signup)
- **Use case**: Backup for stocks

## Performance Metrics

### ROI (Return on Investment)
```
ROI = (Current Value - Cost Basis) / Cost Basis × 100
```

### IRR (Internal Rate of Return)
```
Annualized return accounting for timing of cash flows
```

### Time-Weighted Return
```
Eliminates impact of deposits/withdrawals
Shows true investment performance
```

## Asset Allocation

Default target allocation (customizable):
- **Stocks**: 60%
- **Bonds**: 20%
- **Crypto**: 10%
- **Real Estate**: 5%
- **Cash**: 5%

**Rebalancing Trigger**: ±5% from target

## Tax-Loss Harvesting

**Benefits**:
- Offset capital gains dollar-for-dollar
- Reduce taxable income by up to $3,000/year
- Carry forward unlimited losses

**Wash Sale Rule**:
- Can't buy identical security 30 days before/after sale
- Agent tracks and warns about wash sales
- Suggests alternative investments

## Dividend Tracking

Tracks all dividend and interest payments:
- **Date received**
- **Amount**
- **Reinvested** (DRIP) or cash
- **YTD total**
- **Projected annual income**
- **Yield on cost**

## Data Structure

### Holding Record
```json
{
  "id": "holding-001",
  "assetType": "stock",
  "ticker": "AAPL",
  "name": "Apple Inc.",
  "quantity": 10,
  "costBasis": 150.00,
  "purchaseDate": "2024-01-15",
  "currentPrice": 185.50,
  "lastUpdated": "2025-11-18T10:00:00Z",
  "account": "Vanguard Brokerage"
}
```

## Installation

```bash
# Plugin is ready to use
# Add your first investment using portfolio-analyzer
# Price updates happen automatically when checking portfolio
```

## Design Decisions

**Model Choice**: Sonnet
- Financial analysis requires judgment
- Multi-step calculations with context
- Rebalancing recommendations need reasoning
- Tax strategy requires expertise
- Cost: ~$0.015/1K tokens

**Tools**: Read, Write, Bash, WebFetch
- Read: Load portfolio data
- Write: Save updates
- Bash: Run Python calculations
- WebFetch: Fetch real-time prices

**API Strategy**: Multiple sources
- Yahoo Finance for stocks (free, reliable)
- CoinGecko for crypto (free, comprehensive)
- Alpha Vantage as backup

## Requirements Met

✅ Multi-asset tracking (stocks, bonds, crypto, real estate)
✅ Real-time price updates via API
✅ Portfolio performance (ROI, IRR)
✅ Asset allocation visualization
✅ Rebalancing recommendations
✅ Tax-loss harvesting opportunities
✅ Dividend/interest tracking

## Privacy and Security

- **All data stored locally**: No cloud sync
- **No account credentials**: Manual entry only
- **API keys in environment**: Never in code
- **Price data only**: No trading capability
- **Read-only APIs**: Can't execute trades

## Future Enhancements

- Broker integration (Plaid API)
- Automatic daily price updates
- Email/SMS alerts for rebalancing
- Historical performance charts
- Correlation analysis
- Risk metrics (Sharpe ratio, volatility)
- Scenario analysis (market crash simulation)
- Goal tracking (retirement planning)

## Troubleshooting

**Prices not updating**:
- Check internet connection
- Verify ticker symbol is correct
- API may be rate limited (wait and retry)

**Wrong asset allocation**:
- Update target allocation in settings
- Ensure all holdings have correct asset type
- Rebalancing threshold may be too high

**Missing dividends**:
- Manually add dividend payments
- Check ex-dividend dates
- Enable DRIP tracking if reinvested

**Tax-loss showing incorrect**:
- Verify purchase dates are accurate
- Check cost basis includes fees
- Ensure wash sale period (30 days) considered

---

**Version**: 1.0.0
**Model**: Sonnet (financial analysis)
**Status**: Production-ready
