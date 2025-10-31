# Payment Processing Skill

Expert knowledge for payment gateway integration, PCI DSS compliance, fraud detection, recurring billing, and payment reconciliation following industry standards (PCI DSS, PSD2, NACHA).

## Overview

This skill provides comprehensive patterns, methodologies, and best practices for implementing secure, compliant, and scalable payment processing systems across multiple payment gateways and methods.

## Core Payment Gateway Providers

### Stripe
**Best For**: Modern SaaS, subscriptions, marketplaces
**Key Features**:
- Excellent API documentation
- Built-in fraud detection (Radar)
- Support for 135+ currencies
- Strong subscription management
- Payment Links and Checkout
- Connect for marketplaces

**Integration Pattern**:
```javascript
// Client-side tokenization
const stripe = Stripe('pk_test_...');
const {token} = await stripe.createToken(card);

// Server-side charge
const charge = await stripe.charges.create({
  amount: 2000,
  currency: 'usd',
  source: token.id,
  description: 'Order #1234'
});
```

**Webhook Events**:
- `charge.succeeded`
- `charge.failed`
- `payment_intent.succeeded`
- `customer.subscription.created`
- `invoice.payment_succeeded`

### PayPal
**Best For**: Consumer payments, international, brand recognition
**Key Features**:
- High consumer trust
- PayPal wallet integration
- Venmo integration
- Buyer/seller protection
- Currency conversion

**Integration Pattern**:
```javascript
// PayPal REST API
const order = await paypal.orders.create({
  intent: 'CAPTURE',
  purchase_units: [{
    amount: {
      currency_code: 'USD',
      value: '20.00'
    }
  }]
});

// PayPal Smart Buttons
paypal.Buttons({
  createOrder: (data, actions) => {
    return actions.order.create({...});
  },
  onApprove: (data, actions) => {
    return actions.order.capture();
  }
}).render('#paypal-button');
```

### Square
**Best For**: Point-of-sale, omnichannel retail
**Key Features**:
- Unified POS and online payments
- Hardware integration (terminals, readers)
- Inventory management
- Staff management
- Customer directory

**Integration Pattern**:
```javascript
// Square Web Payments SDK
const payments = Square.payments(appId, locationId);
const card = await payments.card();
await card.attach('#card-container');

const result = await card.tokenize();
// Send result.token to server
```

### Adyen
**Best For**: Enterprise, global expansion, high volume
**Key Features**:
- Single integration for 250+ payment methods
- Local acquiring worldwide
- Revenue optimization engine
- Advanced fraud prevention
- Omnichannel (online, POS, mobile)

**Integration Pattern**:
```javascript
// Adyen Drop-in
const checkout = new AdyenCheckout({
  environment: 'test',
  clientKey: 'test_...',
  paymentMethodsResponse: paymentMethods,
  onSubmit: (state, dropin) => {
    makePayment(state.data);
  }
});

checkout.create('dropin').mount('#dropin-container');
```

### Braintree (PayPal Company)
**Best For**: Flexible integration, multiple payment methods
**Key Features**:
- Owned by PayPal (easy PayPal integration)
- Venmo, Apple Pay, Google Pay
- Vault for stored payment methods
- Advanced fraud tools
- GraphQL API

**Integration Pattern**:
```javascript
// Braintree Hosted Fields
braintree.client.create({
  authorization: clientToken
}, (err, clientInstance) => {
  braintree.hostedFields.create({
    client: clientInstance,
    fields: {
      number: {selector: '#card-number'},
      cvv: {selector: '#cvv'},
      expirationDate: {selector: '#expiration'}
    }
  });
});
```

## PCI DSS Compliance Levels

### Compliance Level Matrix

| Level | Transaction Volume (Annual) | Assessment Requirements |
|-------|----------------------------|------------------------|
| 1 | > 6 million | Annual ROC by QSA, quarterly ASV scans |
| 2 | 1-6 million | Annual SAQ, quarterly ASV scans |
| 3 | 20,000-1 million (e-commerce) | Annual SAQ, quarterly ASV scans |
| 4 | < 20,000 (e-commerce) or < 1 million (other) | Annual SAQ, quarterly ASV scans |

### PCI DSS 4.0 Requirements (2024)

**Build and Maintain Secure Networks**:
1. Install and maintain network security controls
2. Apply secure configurations to all system components

**Protect Cardholder Data**:
3. Protect stored account data
4. Protect cardholder data with strong cryptography during transmission

**Maintain a Vulnerability Management Program**:
5. Protect all systems and networks from malicious software
6. Develop and maintain secure systems and software

**Implement Strong Access Control Measures**:
7. Restrict access to system components and cardholder data by business need to know
8. Identify users and authenticate access to system components
9. Restrict physical access to cardholder data

**Regularly Monitor and Test Networks**:
10. Log and monitor all access to system components and cardholder data
11. Test security of systems and networks regularly

**Maintain an Information Security Policy**:
12. Support information security with organizational policies and programs

### PCI Compliance Strategies

**Strategy 1: Reduce Scope (Recommended)**
```
┌─────────────────────────────────────────────┐
│         Out of PCI Scope                    │
│  ┌──────────────────────────────────────┐  │
│  │  Web Application                     │  │
│  │  (No card data stored or processed)  │  │
│  └──────────┬───────────────────────────┘  │
│             │                                │
│             │ Token/Customer ID only         │
│             │                                │
│  ┌──────────▼───────────────────────────┐  │
│  │  Payment Gateway (Stripe, PayPal)    │  │
│  │  (PCI DSS Level 1 Certified)         │  │
│  └──────────────────────────────────────┘  │
└─────────────────────────────────────────────┘
```

**Never Store**:
- Full magnetic stripe data
- CAV2/CVC2/CVV2/CID
- PIN or PIN block

**Can Store (Encrypted)**:
- Primary Account Number (PAN) - only if business need
- Cardholder name
- Expiration date
- Service code

**Best Practice**: Use tokenization to avoid storing card data entirely.

### SAQ Types

**SAQ A**: Card-not-present, all functions outsourced
- Merchant website redirects to payment page
- No card data touches merchant systems
- Easiest compliance path

**SAQ A-EP**: E-commerce using third-party payment page
- Payment page hosted by third party
- Some data may touch merchant systems (via JavaScript)

**SAQ D**: All other merchants
- Most comprehensive assessment
- Requires all 12 PCI requirements

## Payment Methods

### Credit/Debit Cards

**Card Networks**:
- Visa
- Mastercard
- American Express
- Discover
- Diners Club
- JCB
- UnionPay

**Card Validation**:
```javascript
// Luhn algorithm for card number validation
function validateCard(cardNumber) {
  const digits = cardNumber.replace(/\D/g, '');
  let sum = 0;
  let isEven = false;

  for (let i = digits.length - 1; i >= 0; i--) {
    let digit = parseInt(digits[i]);

    if (isEven) {
      digit *= 2;
      if (digit > 9) digit -= 9;
    }

    sum += digit;
    isEven = !isEven;
  }

  return sum % 10 === 0;
}

// Card type detection
function getCardType(cardNumber) {
  const patterns = {
    visa: /^4/,
    mastercard: /^5[1-5]|^2[2-7]/,
    amex: /^3[47]/,
    discover: /^6(?:011|5)/,
    diners: /^3(?:0[0-5]|[68])/,
    jcb: /^35/
  };

  for (const [type, pattern] of Object.entries(patterns)) {
    if (pattern.test(cardNumber)) return type;
  }

  return 'unknown';
}
```

### ACH (Automated Clearing House)

**Best For**: Recurring payments, large amounts, B2B
**Timing**: 3-5 business days
**Cost**: Very low ($0.25-$1.50 per transaction)

**ACH Payment Types**:
- **CCD** (Cash Concentration or Disbursement): B2B
- **PPD** (Prearranged Payment and Deposit): Consumer
- **WEB** (Internet-Initiated): Online consumer
- **TEL** (Telephone-Initiated): Phone orders

**NACHA Requirements**:
```javascript
// ACH authorization requirements
const achAuthorization = {
  // Required fields
  customerName: 'John Doe',
  routingNumber: '123456789',
  accountNumber: '987654321',
  accountType: 'checking', // or 'savings'

  // Authorization proof
  authorizationType: 'web', // web, voice, written
  authorizationDate: '2025-01-20',

  // Required disclosure
  termsAccepted: true,
  revokeInstructions: 'Customer may revoke by calling...',

  // SEC code
  secCode: 'WEB'
};
```

### Digital Wallets

**Apple Pay**:
```javascript
// Apple Pay integration
const request = {
  countryCode: 'US',
  currencyCode: 'USD',
  supportedNetworks: ['visa', 'masterCard', 'amex'],
  merchantCapabilities: ['supports3DS'],
  total: {
    label: 'Your Store',
    amount: '19.99'
  }
};

const session = new ApplePaySession(3, request);
session.begin();
```

**Google Pay**:
```javascript
// Google Pay integration
const googlePayClient = new google.payments.api.PaymentsClient({
  environment: 'PRODUCTION'
});

const paymentDataRequest = {
  apiVersion: 2,
  apiVersionMinor: 0,
  allowedPaymentMethods: [{
    type: 'CARD',
    parameters: {
      allowedAuthMethods: ['PAN_ONLY', 'CRYPTOGRAM_3DS'],
      allowedCardNetworks: ['MASTERCARD', 'VISA']
    }
  }],
  transactionInfo: {
    totalPriceStatus: 'FINAL',
    totalPrice: '19.99',
    currencyCode: 'USD'
  }
};
```

### Buy Now Pay Later (BNPL)

**Providers**:
- Affirm
- Afterpay
- Klarna
- PayPal Pay in 4

**Use Cases**:
- Higher average order value (AOV)
- Reduce cart abandonment
- Attract younger demographics
- No credit card required

**Integration Example (Affirm)**:
```javascript
// Affirm checkout
affirm.checkout({
  merchant: {
    user_confirmation_url: 'https://example.com/confirm',
    user_cancel_url: 'https://example.com/cancel'
  },
  items: [{
    display_name: 'Product Name',
    sku: 'PROD-001',
    unit_price: 5000, // cents
    qty: 1
  }],
  billing: {...},
  shipping: {...},
  total: 5000
});

affirm.checkout.open();
```

### Cryptocurrency

**Popular Processors**:
- Coinbase Commerce
- BitPay
- CoinGate
- NOWPayments

**Considerations**:
- Price volatility
- Settlement timing
- Regulatory compliance (varies by jurisdiction)
- Tax implications
- Refund complexity

## Fraud Detection Patterns

### Velocity Checks

**Purpose**: Detect unusual transaction patterns

```javascript
// Velocity check implementation
async function checkVelocity(customerId, amount, timeWindow = 3600) {
  // Check 1: Transaction count in time window
  const recentTxCount = await db.transactions.count({
    customerId,
    createdAt: { $gte: Date.now() - timeWindow * 1000 }
  });

  if (recentTxCount > 5) {
    return {
      allowed: false,
      reason: 'Too many transactions in short time period',
      riskScore: 80
    };
  }

  // Check 2: Total amount in time window
  const recentTxSum = await db.transactions.aggregate([
    {
      $match: {
        customerId,
        createdAt: { $gte: new Date(Date.now() - timeWindow * 1000) }
      }
    },
    {
      $group: {
        _id: null,
        total: { $sum: '$amount' }
      }
    }
  ]);

  if (recentTxSum[0]?.total > 10000) {
    return {
      allowed: false,
      reason: 'Transaction volume exceeds threshold',
      riskScore: 85
    };
  }

  // Check 3: Unique cards used
  const uniqueCards = await db.transactions.distinct('cardFingerprint', {
    customerId,
    createdAt: { $gte: new Date(Date.now() - timeWindow * 1000) }
  });

  if (uniqueCards.length > 3) {
    return {
      allowed: false,
      reason: 'Too many different cards used',
      riskScore: 90
    };
  }

  return { allowed: true, riskScore: 10 };
}
```

### Address Verification Service (AVS)

**AVS Response Codes**:
| Code | Meaning | Action |
|------|---------|--------|
| Y | Address and ZIP match | Accept |
| A | Address matches, ZIP doesn't | Review |
| Z | ZIP matches, address doesn't | Review |
| N | Neither address nor ZIP match | Decline |
| U | Information unavailable | Review |
| R | Retry (system unavailable) | Retry |

**AVS Implementation**:
```javascript
function evaluateAVS(avsCode, cardType) {
  const highRiskCodes = ['N', 'C', 'E'];
  const mediumRiskCodes = ['A', 'Z', 'W', 'P'];
  const acceptableCodes = ['Y', 'X', 'D', 'M'];

  // American Express has different AVS codes
  if (cardType === 'amex') {
    if (['Y', 'D', 'M'].includes(avsCode)) return 'accept';
  }

  if (highRiskCodes.includes(avsCode)) {
    return 'decline'; // or 'review' depending on risk tolerance
  }

  if (mediumRiskCodes.includes(avsCode)) {
    return 'review'; // Manual review or additional checks
  }

  if (acceptableCodes.includes(avsCode)) {
    return 'accept';
  }

  return 'review'; // Unknown codes
}
```

### CVV/CVC Verification

**CVV Response Codes**:
| Code | Meaning | Action |
|------|---------|--------|
| M | CVV matches | Accept |
| N | CVV doesn't match | Decline |
| P | CVV not processed | Review |
| S | CVV should be on card but wasn't provided | Decline |
| U | Issuer doesn't support CVV | Accept (with caution) |

**Best Practice**: Always require CVV for card-not-present transactions.

### 3D Secure (3DS)

**3D Secure 2.0 Flow**:
```
Customer → Merchant → 3DS Server → Card Issuer
                ↓
        Authentication Challenge (if needed)
                ↓
         Strong Customer Authentication
                ↓
         Transaction Authorized
```

**Benefits**:
- Shifts fraud liability to issuer
- Required for PSD2 (EU) compliance
- Reduces chargebacks
- Supports frictionless authentication

**Implementation (Stripe)**:
```javascript
// Create PaymentIntent with 3DS
const paymentIntent = await stripe.paymentIntents.create({
  amount: 2000,
  currency: 'eur',
  payment_method_types: ['card'],
  payment_method_options: {
    card: {
      request_three_d_secure: 'automatic' // or 'any'
    }
  }
});

// Client-side confirmation
const result = await stripe.confirmCardPayment(
  paymentIntent.client_secret,
  {
    payment_method: {
      card: cardElement,
      billing_details: {...}
    }
  }
);
```

### Risk Scoring Model

```javascript
function calculateRiskScore(transaction) {
  let score = 0;
  const factors = [];

  // Factor 1: Transaction amount
  if (transaction.amount > 500) {
    score += 20;
    factors.push('High transaction amount');
  }

  // Factor 2: New customer
  if (transaction.customerAge < 30) { // days
    score += 15;
    factors.push('New customer account');
  }

  // Factor 3: Shipping vs billing mismatch
  if (transaction.shippingAddress !== transaction.billingAddress) {
    score += 25;
    factors.push('Shipping/billing address mismatch');
  }

  // Factor 4: High-risk country
  const highRiskCountries = ['XX', 'YY', 'ZZ'];
  if (highRiskCountries.includes(transaction.country)) {
    score += 30;
    factors.push('High-risk country');
  }

  // Factor 5: Unusual time
  const hour = new Date().getHours();
  if (hour >= 2 && hour <= 5) {
    score += 10;
    factors.push('Unusual transaction time');
  }

  // Factor 6: Email/phone validation
  if (!transaction.emailVerified) {
    score += 15;
    factors.push('Unverified email');
  }

  // Factor 7: Device fingerprint
  if (transaction.deviceFingerprint in knownFraudDevices) {
    score += 50;
    factors.push('Known fraud device');
  }

  // Factor 8: IP reputation
  if (transaction.ipReputationScore > 70) {
    score += 30;
    factors.push('Poor IP reputation');
  }

  return {
    score,
    risk: score < 30 ? 'low' : score < 60 ? 'medium' : 'high',
    factors,
    action: score < 30 ? 'accept' : score < 60 ? 'review' : 'decline'
  };
}
```

## Recurring Billing & Subscription Management

### Subscription Models

**1. Fixed Recurring**:
- Monthly: $29/month
- Annual: $290/year (16% savings)
- Best for: SaaS, memberships

**2. Usage-Based**:
- Pay per API call, GB storage, etc.
- Best for: Cloud services, utilities

**3. Tiered**:
- Starter: $10/month (10 users)
- Professional: $30/month (50 users)
- Enterprise: Custom pricing

**4. Freemium**:
- Free tier with limitations
- Paid tiers unlock features

**5. Hybrid**:
- Base fee + usage charges
- Example: $50/month + $0.10 per transaction

### Subscription Lifecycle

```
┌──────────────────────────────────────────────┐
│              TRIAL (optional)                │
│  • 7-14 days free                            │
│  • May or may not require card              │
└────────────┬─────────────────────────────────┘
             │
             ▼
┌──────────────────────────────────────────────┐
│              ACTIVE                          │
│  • Billing every period                     │
│  • Full access                               │
└────────────┬─────────────────────────────────┘
             │
             ├─► UPGRADE/DOWNGRADE (prorate)
             │
             ├─► PAYMENT FAILURE
             │        │
             │        ▼
             │   ┌─────────────────────────┐
             │   │  PAST DUE               │
             │   │  • Retry payment        │
             │   │  • Send reminders       │
             │   └──────┬──────────────────┘
             │          │
             │          ├─► SUCCESS → ACTIVE
             │          │
             │          └─► FAILURE (after retries)
             │                   │
             │                   ▼
             │          ┌─────────────────┐
             │          │  CANCELED       │
             │          │  • Access ends  │
             │          └─────────────────┘
             │
             └─► CUSTOMER CANCELS
                      │
                      ▼
             ┌──────────────────────┐
             │  CANCELED            │
             │  • End of period or  │
             │    immediate         │
             └──────────────────────┘
```

### Proration Logic

```javascript
function calculateProration(currentPlan, newPlan, billingCycleStart) {
  const now = Date.now();
  const cycleEnd = new Date(billingCycleStart);
  cycleEnd.setMonth(cycleEnd.getMonth() + 1);

  const totalCycleDays = (cycleEnd - billingCycleStart) / (1000 * 60 * 60 * 24);
  const remainingDays = (cycleEnd - now) / (1000 * 60 * 60 * 24);

  // Unused amount from current plan
  const currentPlanUnused = (currentPlan.price / totalCycleDays) * remainingDays;

  // Cost for remaining period on new plan
  const newPlanCost = (newPlan.price / totalCycleDays) * remainingDays;

  // Amount to charge/credit now
  const proratedAmount = newPlanCost - currentPlanUnused;

  return {
    proratedAmount: Math.max(0, proratedAmount),
    creditApplied: Math.max(0, -proratedAmount),
    nextBillingDate: cycleEnd,
    nextBillingAmount: newPlan.price
  };
}
```

### Dunning Management

**Dunning**: Process of recovering failed subscription payments

```javascript
const dunningSchedule = [
  { day: 0, action: 'retry_immediately' },
  { day: 3, action: 'retry_and_email' },
  { day: 5, action: 'retry_and_email' },
  { day: 7, action: 'retry_and_email_urgent' },
  { day: 10, action: 'retry_and_email_final_notice' },
  { day: 14, action: 'cancel_subscription' }
];

async function handleFailedPayment(subscription, attempt = 1) {
  const schedule = dunningSchedule[attempt - 1];

  if (!schedule) {
    // Max retries exceeded
    await cancelSubscription(subscription.id, 'payment_failure');
    return;
  }

  // Wait for scheduled day
  await scheduleTask(schedule.day * 24 * 60 * 60 * 1000, async () => {
    // Retry payment
    const result = await retryPayment(subscription);

    if (result.success) {
      await reactivateSubscription(subscription.id);
      await sendEmail(subscription.customerId, 'payment_success');
    } else {
      // Send appropriate email
      if (schedule.action.includes('email')) {
        await sendDunningEmail(
          subscription.customerId,
          schedule.action.replace('retry_and_', '')
        );
      }

      // Schedule next attempt
      await handleFailedPayment(subscription, attempt + 1);
    }
  });
}
```

### Subscription Webhooks

```javascript
// Handle subscription events
app.post('/webhooks/stripe', async (req, res) => {
  const sig = req.headers['stripe-signature'];
  const event = stripe.webhooks.constructEvent(
    req.body,
    sig,
    webhookSecret
  );

  switch (event.type) {
    case 'customer.subscription.created':
      await handleSubscriptionCreated(event.data.object);
      break;

    case 'customer.subscription.updated':
      await handleSubscriptionUpdated(event.data.object);
      break;

    case 'customer.subscription.deleted':
      await handleSubscriptionCanceled(event.data.object);
      break;

    case 'invoice.payment_succeeded':
      await handlePaymentSucceeded(event.data.object);
      break;

    case 'invoice.payment_failed':
      await handlePaymentFailed(event.data.object);
      break;

    case 'customer.subscription.trial_will_end':
      await sendTrialEndingEmail(event.data.object);
      break;
  }

  res.json({ received: true });
});
```

## Payment Reconciliation

### Reconciliation Process

```
┌─────────────────────────────────────────────┐
│  1. EXPORT TRANSACTIONS                     │
│     • From internal database                │
│     • Date range: Yesterday                 │
└────────────┬────────────────────────────────┘
             │
             ▼
┌─────────────────────────────────────────────┐
│  2. DOWNLOAD GATEWAY REPORTS                │
│     • Stripe: Balance transactions          │
│     • PayPal: Transaction history           │
│     • Same date range                       │
└────────────┬────────────────────────────────┘
             │
             ▼
┌─────────────────────────────────────────────┐
│  3. MATCH TRANSACTIONS                      │
│     • By transaction ID                     │
│     • By amount + timestamp                 │
│     • Flag unmatched                        │
└────────────┬────────────────────────────────┘
             │
             ▼
┌─────────────────────────────────────────────┐
│  4. INVESTIGATE DISCREPANCIES               │
│     • Missing transactions                  │
│     • Amount mismatches                     │
│     • Status differences                    │
└────────────┬────────────────────────────────┘
             │
             ▼
┌─────────────────────────────────────────────┐
│  5. RECONCILE FEES                          │
│     • Gateway fees                          │
│     • Network fees                          │
│     • Calculate net settlement              │
└────────────┬────────────────────────────────┘
             │
             ▼
┌─────────────────────────────────────────────┐
│  6. UPDATE ACCOUNTING                       │
│     • Journal entries                       │
│     • Account for fees                      │
│     • Match bank deposits                   │
└─────────────────────────────────────────────┘
```

### Reconciliation Script

```javascript
async function reconcilePayments(date) {
  // 1. Get internal transactions
  const internalTxs = await db.transactions.find({
    createdAt: {
      $gte: startOfDay(date),
      $lt: endOfDay(date)
    },
    status: 'succeeded'
  });

  // 2. Get gateway transactions
  const stripeTxs = await stripe.balanceTransactions.list({
    created: {
      gte: startOfDay(date) / 1000,
      lt: endOfDay(date) / 1000
    }
  });

  // 3. Match transactions
  const matched = [];
  const unmatched = {
    internal: [],
    gateway: []
  };

  const gatewayMap = new Map(
    stripeTxs.data.map(tx => [tx.source, tx])
  );

  for (const internalTx of internalTxs) {
    const gatewayTx = gatewayMap.get(internalTx.gatewayId);

    if (!gatewayTx) {
      unmatched.internal.push(internalTx);
      continue;
    }

    // Check amounts match
    if (internalTx.amount !== gatewayTx.amount) {
      matched.push({
        internal: internalTx,
        gateway: gatewayTx,
        issue: 'amount_mismatch',
        difference: internalTx.amount - gatewayTx.amount
      });
    } else {
      matched.push({
        internal: internalTx,
        gateway: gatewayTx,
        issue: null
      });
    }

    gatewayMap.delete(internalTx.gatewayId);
  }

  // Remaining gateway transactions are unmatched
  unmatched.gateway = Array.from(gatewayMap.values());

  // 4. Calculate totals
  const summary = {
    date,
    totalInternal: internalTxs.reduce((sum, tx) => sum + tx.amount, 0),
    totalGateway: stripeTxs.data.reduce((sum, tx) => sum + tx.amount, 0),
    totalFees: stripeTxs.data.reduce((sum, tx) => sum + tx.fee, 0),
    netSettlement: stripeTxs.data.reduce((sum, tx) => sum + tx.net, 0),
    matchedCount: matched.filter(m => !m.issue).length,
    unmatchedCount: unmatched.internal.length + unmatched.gateway.length,
    issues: matched.filter(m => m.issue).length
  };

  // 5. Generate report
  const report = {
    summary,
    matched,
    unmatched,
    recommendations: generateRecommendations(summary, unmatched)
  };

  await saveReconciliationReport(report);

  if (summary.unmatchedCount > 0 || summary.issues > 0) {
    await notifyFinanceTeam(report);
  }

  return report;
}
```

### Settlement Timing

**Payment Gateway Settlement Times**:
| Gateway | Standard | Instant (if available) |
|---------|----------|----------------------|
| Stripe | 2 business days | Instant (1.5% fee) |
| PayPal | 1 business day | Instant (1% fee) |
| Square | 1-2 business days | Instant (1.5% fee) |
| Adyen | 2-3 business days | N/A |
| Braintree | 1-2 business days | Next day (1% fee) |

## Webhook Security

### Webhook Verification

```javascript
// Stripe webhook verification
app.post('/webhooks/stripe', express.raw({type: 'application/json'}), (req, res) => {
  const sig = req.headers['stripe-signature'];

  let event;
  try {
    event = stripe.webhooks.constructEvent(
      req.body,
      sig,
      webhookSecret
    );
  } catch (err) {
    console.log(`Webhook signature verification failed: ${err.message}`);
    return res.status(400).send(`Webhook Error: ${err.message}`);
  }

  // Handle event
  handleWebhookEvent(event);

  res.json({ received: true });
});

// PayPal webhook verification
async function verifyPayPalWebhook(req) {
  const verifyRequest = {
    auth_algo: req.headers['paypal-auth-algo'],
    cert_url: req.headers['paypal-cert-url'],
    transmission_id: req.headers['paypal-transmission-id'],
    transmission_sig: req.headers['paypal-transmission-sig'],
    transmission_time: req.headers['paypal-transmission-time'],
    webhook_id: webhookId,
    webhook_event: req.body
  };

  const response = await paypal.notification.webhook.verify(verifyRequest);
  return response.verification_status === 'SUCCESS';
}
```

### Webhook Best Practices

1. **Verify Signatures**: Always verify webhook signatures
2. **Idempotency**: Handle duplicate webhooks gracefully
3. **Async Processing**: Process webhooks asynchronously
4. **Retry Logic**: Implement retry logic for failures
5. **Logging**: Log all webhook events for debugging
6. **Monitoring**: Alert on webhook failures

```javascript
// Idempotent webhook handler
async function handleWebhookEvent(event) {
  // Check if already processed
  const existing = await db.webhookEvents.findOne({
    eventId: event.id
  });

  if (existing) {
    console.log(`Webhook ${event.id} already processed`);
    return { status: 'duplicate' };
  }

  // Store event immediately
  await db.webhookEvents.create({
    eventId: event.id,
    type: event.type,
    data: event.data,
    processed: false,
    receivedAt: new Date()
  });

  try {
    // Process event
    await processEvent(event);

    // Mark as processed
    await db.webhookEvents.updateOne(
      { eventId: event.id },
      {
        processed: true,
        processedAt: new Date()
      }
    );

    return { status: 'success' };
  } catch (error) {
    // Log error but don't throw
    await db.webhookEvents.updateOne(
      { eventId: event.id },
      {
        error: error.message,
        errorAt: new Date()
      }
    );

    // Queue for retry
    await queueWebhookRetry(event.id);

    return { status: 'error', error: error.message };
  }
}
```

## Multi-Currency & Localization

### Currency Conversion Strategies

**1. Fixed Rate at Time of Purchase**
```javascript
const exchangeRate = await getExchangeRate('EUR', 'USD');
const amountInUSD = amountInEUR * exchangeRate;
```

**2. Dynamic Pricing**
```javascript
const priceMatrix = {
  'USD': 29.99,
  'EUR': 24.99,
  'GBP': 21.99,
  'JPY': 3300
};
```

**3. Automatic Currency Detection**
```javascript
function detectCurrency(ipAddress, billingCountry) {
  const countryToCurrency = {
    'US': 'USD',
    'GB': 'GBP',
    'DE': 'EUR',
    'JP': 'JPY',
    // ...
  };

  return countryToCurrency[billingCountry] || 'USD';
}
```

### Local Payment Methods

**Europe**:
- SEPA Direct Debit
- iDEAL (Netherlands)
- Giropay (Germany)
- Bancontact (Belgium)
- Przelewy24 (Poland)

**Asia**:
- Alipay (China)
- WeChat Pay (China)
- PayPay (Japan)
- GrabPay (Southeast Asia)
- PayNow (Singapore)

**Latin America**:
- Boleto (Brazil)
- OXXO (Mexico)
- Mercado Pago

## Refunds & Disputes

### Refund Types

**Full Refund**:
```javascript
const refund = await stripe.refunds.create({
  charge: chargeId,
  reason: 'requested_by_customer'
});
```

**Partial Refund**:
```javascript
const refund = await stripe.refunds.create({
  charge: chargeId,
  amount: 500, // cents
  reason: 'requested_by_customer'
});
```

**Refund Reasons**:
- `requested_by_customer`: Customer requested
- `duplicate`: Duplicate charge
- `fraudulent`: Fraudulent charge

### Chargeback Process

```
Customer disputes → Issuing Bank → Card Network → Acquiring Bank → Merchant

Merchant Response:
1. Gather evidence within 7 days
2. Submit compelling evidence:
   - Proof of delivery
   - Signed receipt
   - Customer communication
   - IP address & geolocation
   - AVS/CVV match results
   - Prior non-disputed transactions
3. Wait for decision (30-90 days)
```

**Chargeback Reason Codes**:
- **10.4**: Fraud (card not present)
- **13.1**: Services not provided
- **13.2**: Canceled recurring
- **13.3**: Not as described
- **13.5**: Misrepresentation

### Dispute Prevention

```javascript
async function preventDispute(transaction) {
  // 1. Clear descriptor
  await updateDescriptor(transaction, {
    name: 'YOUR-BRAND',
    phone: '1-800-XXX-XXXX',
    url: 'support.yourbrand.com'
  });

  // 2. Send confirmation email immediately
  await sendConfirmationEmail(transaction.customerId, {
    amount: transaction.amount,
    descriptor: 'YOUR-BRAND',
    supportContact: 'support@yourbrand.com'
  });

  // 3. Provide excellent customer service
  // 4. Have clear refund policy
  // 5. Use 3D Secure for high-value transactions
  // 6. Keep detailed records
}
```

## Testing Payment Integrations

### Test Card Numbers

**Stripe Test Cards**:
```
Success: 4242 4242 4242 4242
3D Secure: 4000 0027 6000 3184
Declined: 4000 0000 0000 0002
Insufficient funds: 4000 0000 0000 9995
```

**PayPal Sandbox**:
- Use PayPal Developer Dashboard
- Create sandbox accounts
- Test full payment flow

### Test Checklist

- [ ] Successful payment
- [ ] Declined payment
- [ ] Insufficient funds
- [ ] 3D Secure authentication
- [ ] Expired card
- [ ] Invalid CVV
- [ ] Refund (full and partial)
- [ ] Subscription creation
- [ ] Subscription upgrade/downgrade
- [ ] Failed subscription payment
- [ ] Webhook handling
- [ ] Idempotency
- [ ] Currency conversion
- [ ] Tax calculation
- [ ] Promotional codes

## Best Practices

1. **Never Store Card Data**: Use tokenization
2. **Use HTTPS**: All payment pages must use SSL/TLS
3. **Verify Webhooks**: Always verify webhook signatures
4. **Implement Idempotency**: Handle duplicate requests
5. **Log Everything**: Comprehensive logging for debugging
6. **Monitor Transactions**: Real-time monitoring and alerts
7. **Test Thoroughly**: Test all payment scenarios
8. **Plan for Failures**: Graceful error handling
9. **Reconcile Daily**: Daily payment reconciliation
10. **Stay Compliant**: Keep up with PCI DSS requirements

## Security Checklist

- [ ] PCI DSS compliant (appropriate level)
- [ ] Card data never stored in plain text
- [ ] Tokenization implemented
- [ ] HTTPS/TLS 1.2+ everywhere
- [ ] Webhook signature verification
- [ ] Rate limiting on payment endpoints
- [ ] Fraud detection rules active
- [ ] 3D Secure for high-risk transactions
- [ ] Regular security audits
- [ ] Penetration testing (if Level 1)
- [ ] Security awareness training
- [ ] Incident response plan
