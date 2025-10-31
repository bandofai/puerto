# Payment Integration Specialist Plugin

Comprehensive payment processing system with secure gateway integration, PCI DSS compliance, fraud prevention, and financial reconciliation.

## Overview

This plugin provides expert-level payment processing capabilities including integration with major payment gateways (Stripe, PayPal, Square, Adyen, Braintree), PCI DSS compliance assessments, advanced fraud detection, and automated payment reconciliation.

## Agents

### 1. Gateway Integrator (Sonnet)
**Purpose**: Integrate payment gateways with secure, PCI-compliant implementations

**Use When**:
- Setting up new payment gateway integration
- Implementing checkout flows
- Adding tokenization for card security
- Creating webhook handlers
- Supporting multiple payment methods

**Key Features**:
- Stripe, PayPal, Square, Adyen, Braintree integration patterns
- Client-side tokenization (never handle raw card data)
- Server-side payment processing
- Webhook signature verification
- Idempotency key handling
- 3D Secure integration
- Multi-currency support

**Example Usage**:
```
@gateway-integrator integrate Stripe payment processing with credit cards and ACH
@gateway-integrator add PayPal as secondary payment method
@gateway-integrator implement webhook handlers for payment events
```

**Deliverables**:
- Payment processing endpoints
- Webhook handlers with security verification
- Client-side checkout components
- Environment configuration guide
- Testing documentation with test cards

### 2. Compliance Specialist (Sonnet)
**Purpose**: Ensure PCI DSS compliance and payment security

**Use When**:
- Starting new payment integration project
- Preparing for PCI DSS assessment
- Conducting security audit
- Completing SAQ questionnaires
- Annual compliance review

**Key Features**:
- PCI DSS level determination (1, 2, 3, 4)
- SAQ type identification (A, A-EP, D)
- 12 PCI requirements assessment
- Security vulnerability scanning
- Compliance gap analysis
- Remediation recommendations
- Policy templates

**Example Usage**:
```
@compliance-specialist assess our PCI DSS compliance level
@compliance-specialist complete SAQ A questionnaire
@compliance-specialist audit payment system security
@compliance-specialist generate compliance report
```

**Deliverables**:
- PCI DSS assessment report
- SAQ questionnaire (if applicable)
- Remediation checklist with priorities
- Security policy templates
- Vendor assessment documentation
- Compliance maintenance plan

### 3. Fraud Preventer (Sonnet)
**Purpose**: Implement fraud detection and prevention systems

**Use When**:
- Experiencing fraudulent transactions
- Need to reduce chargeback rate
- Implementing risk-based authentication
- Setting up fraud monitoring
- Creating manual review process

**Key Features**:
- Multi-factor risk scoring engine (10+ factors)
- Velocity checks (customer, card, IP, amount)
- AVS and CVV validation
- 3D Secure integration for high-risk transactions
- Device fingerprinting
- Geographic risk assessment
- Manual review queue and dashboard
- Fraud alert system (Slack, email)

**Example Usage**:
```
@fraud-preventer implement fraud detection with risk scoring
@fraud-preventer add velocity checks for transaction limits
@fraud-preventer create manual review dashboard
@fraud-preventer configure 3D Secure for high-risk transactions
```

**Deliverables**:
- Risk scoring engine with configurable weights
- Fraud detection middleware
- Device fingerprinting client library
- Manual review dashboard
- Alert system configuration
- Testing scenarios with risk scores

### 4. Reconciliation Manager (Haiku)
**Purpose**: Automate payment reconciliation and settlement tracking

**Use When**:
- Need daily payment reconciliation
- Tracking settlement deposits
- Identifying transaction discrepancies
- Generating accounting reports
- Exporting to accounting systems

**Key Features**:
- Automated daily reconciliation
- Transaction matching (internal vs gateway)
- Discrepancy detection and investigation
- Settlement tracking (expected vs actual)
- Fee analysis and breakdown
- Accounting exports (QuickBooks, CSV)
- Alert system for mismatches

**Example Usage**:
```
@reconciliation-manager set up daily reconciliation for Stripe
@reconciliation-manager investigate payment discrepancies from yesterday
@reconciliation-manager generate accounting export for January
@reconciliation-manager track settlement deposits
```

**Deliverables**:
- Automated reconciliation service
- Scheduled daily jobs
- Discrepancy investigation reports
- Settlement tracking dashboard
- Accounting journal entries
- Export formats (IIF, CSV)

## Skill Reference

The payment processing skill (`SKILL.md`) provides comprehensive knowledge on:

### Payment Gateway Providers
- Stripe (best for SaaS, subscriptions)
- PayPal (consumer trust, international)
- Square (point-of-sale, omnichannel)
- Adyen (enterprise, global)
- Braintree (flexible, multiple methods)

### PCI DSS Compliance
- Compliance levels and requirements
- SAQ types and eligibility
- 12 PCI DSS 4.0 requirements
- Scope reduction strategies
- Tokenization best practices

### Payment Methods
- Credit/debit cards (Visa, Mastercard, Amex, etc.)
- ACH (bank transfers)
- Digital wallets (Apple Pay, Google Pay)
- Buy Now Pay Later (Affirm, Afterpay, Klarna)
- Cryptocurrency

### Fraud Detection
- Velocity checks
- AVS (Address Verification Service)
- CVV/CVC verification
- 3D Secure (SCA/PSD2)
- Risk scoring models
- Device fingerprinting

### Recurring Billing
- Subscription models
- Proration logic
- Dunning management
- Subscription lifecycle
- Failed payment handling

### Reconciliation
- Transaction matching algorithms
- Discrepancy investigation
- Settlement timing by gateway
- Fee calculation
- Accounting integration

### Security
- Webhook verification
- Tokenization vs encryption
- TLS/HTTPS requirements
- Data retention policies
- Incident response

## Workflow Examples

### New Payment Integration
```bash
# 1. Design integration approach
@gateway-integrator assess current system and recommend gateway

# 2. Implement payment processing
@gateway-integrator integrate Stripe with credit cards and ACH

# 3. Ensure compliance
@compliance-specialist assess PCI DSS requirements and complete SAQ A

# 4. Add fraud protection
@fraud-preventer implement risk scoring and velocity checks

# 5. Set up reconciliation
@reconciliation-manager configure daily reconciliation and reports
```

### Compliance Audit
```bash
# 1. Assess current compliance
@compliance-specialist determine PCI level and SAQ type

# 2. Review payment integration
@gateway-integrator audit payment processing implementation

# 3. Identify security gaps
@compliance-specialist complete 12 PCI requirements assessment

# 4. Review fraud controls
@fraud-preventer audit fraud detection coverage

# 5. Generate compliance report
@compliance-specialist create remediation plan with priorities
```

### Fraud Investigation
```bash
# 1. Analyze fraud patterns
@fraud-preventer review recent fraudulent transactions

# 2. Adjust risk scoring
@fraud-preventer tune risk model based on fraud data

# 3. Implement additional controls
@fraud-preventer add 3D Secure for high-risk countries

# 4. Set up monitoring
@fraud-preventer configure alerts for suspicious patterns

# 5. Reconcile chargebacks
@reconciliation-manager track disputed transactions
```

## Installation

1. Copy plugin to your Puerto plugins directory:
   ```bash
   cp -r payment-integration-specialist ~/.puerto/plugins/
   ```

2. Agents are automatically available:
   - `@gateway-integrator`
   - `@compliance-specialist`
   - `@fraud-preventer`
   - `@reconciliation-manager`

3. Install dependencies for your stack:
   ```bash
   # Node.js
   npm install stripe @paypal/checkout-server-sdk square

   # Python
   pip install stripe paypal-checkout-serversdk squareup
   ```

## Environment Variables

Required environment variables for payment processing:

```bash
# Stripe
STRIPE_SECRET_KEY=sk_live_...
STRIPE_PUBLISHABLE_KEY=pk_live_...
STRIPE_WEBHOOK_SECRET=whsec_...

# PayPal
PAYPAL_CLIENT_ID=...
PAYPAL_CLIENT_SECRET=...
PAYPAL_WEBHOOK_ID=...

# Square
SQUARE_ACCESS_TOKEN=...
SQUARE_LOCATION_ID=...

# Alerts
SLACK_FRAUD_WEBHOOK=...
FRAUD_ALERT_EMAILS=finance@example.com,security@example.com
FINANCE_TEAM_EMAIL=finance@example.com

# Application
NODE_ENV=production
BASE_URL=https://yourapp.com
```

## Security Best Practices

### Never Store
- Full magnetic stripe data
- CAV2/CVC2/CVV2/CID codes
- PIN or PIN blocks

### Always Use
- HTTPS/TLS 1.2+ for all payment pages
- Tokenization (not encryption) for card data
- Webhook signature verification
- Strong authentication (MFA for admin)
- Rate limiting on payment endpoints

### Required Validations
- AVS (Address Verification Service)
- CVV/CVC check
- 3D Secure for high-risk transactions
- Velocity checks (prevent abuse)
- Device fingerprinting

### Compliance Requirements
- PCI DSS SAQ completion (annual)
- ASV vulnerability scans (quarterly)
- Security awareness training (annual)
- Incident response plan documented
- Vendor management program

## Testing

### Test Cards

**Stripe**:
- Success: `4242 4242 4242 4242`
- Declined: `4000 0000 0000 0002`
- 3D Secure: `4000 0027 6000 3184`
- Insufficient Funds: `4000 0000 0000 9995`

**PayPal**: Use PayPal Sandbox accounts

**Square**: Use Square Sandbox environment

### Test Scenarios
1. Successful payment flow
2. Declined card handling
3. 3D Secure authentication
4. Refund processing (full and partial)
5. Webhook event handling
6. Fraud detection triggers
7. Reconciliation matching
8. Settlement tracking

## Monitoring & Alerts

### Key Metrics
- Transaction success rate (target: >98%)
- Fraud detection rate (target: <2%)
- False positive rate (target: <5%)
- Reconciliation match rate (target: >99%)
- Average response time (target: <500ms)
- Settlement timing (2-3 business days)

### Alerts
- Failed payments (immediate)
- High fraud risk transactions (immediate)
- Reconciliation discrepancies (daily)
- Settlement delays (daily)
- Compliance issues (immediate)
- System errors (immediate)

## Maintenance

### Daily
- Review reconciliation reports
- Monitor fraud alerts
- Check failed payments
- Review manual review queue

### Weekly
- Analyze fraud patterns
- Review risk scoring effectiveness
- Check settlement deposits
- Update transaction trends

### Monthly
- Review and tune fraud rules
- Analyze payment method performance
- Check gateway fees and costs
- Update risk model weights

### Quarterly
- ASV vulnerability scans (PCI requirement)
- Review firewall rules
- Audit user access
- Test disaster recovery

### Annual
- Complete SAQ reassessment
- Security awareness training
- Full compliance review
- Penetration testing (if Level 1)
- Policy reviews and updates

## Troubleshooting

### Payment Failures
1. Check webhook signature verification
2. Verify API keys are correct
3. Confirm HTTPS is enforced
4. Review error logs
5. Test with test cards

### Reconciliation Issues
1. Verify date ranges match
2. Check timezone conversions
3. Account for refund timing
4. Review fee calculations
5. Investigate partial captures

### Fraud Detection Problems
1. Review false positive rate
2. Adjust risk score thresholds
3. Check velocity check timing
4. Verify device fingerprinting
5. Update country risk lists

### Compliance Gaps
1. Review PCI requirements
2. Check for stored card data
3. Verify encryption/tokenization
4. Audit access controls
5. Update security policies

## Resources

### Documentation
- [Stripe API Documentation](https://stripe.com/docs/api)
- [PayPal Developer Docs](https://developer.paypal.com/docs/)
- [PCI DSS Requirements](https://www.pcisecuritystandards.org/)
- [OWASP Payment Security](https://owasp.org/www-project-payment-security/)

### Tools
- Stripe Dashboard: Transaction monitoring
- PayPal Dashboard: Payment management
- PCI SSC: Compliance resources
- OWASP ZAP: Security testing

## License

MIT License - see LICENSE file for details

## Contributing

Contributions welcome! Please:
1. Follow existing agent patterns
2. Update SKILL.md with new knowledge
3. Add test scenarios
4. Document security considerations
5. Submit pull request

## Changelog

### Version 1.0.0 (2025-01-29)
- Initial release
- Gateway integrator agent
- Compliance specialist agent
- Fraud preventer agent
- Reconciliation manager agent
- Comprehensive payment processing skill
- Test scenarios and documentation
