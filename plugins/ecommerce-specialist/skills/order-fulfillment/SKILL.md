# Order Fulfillment Skill

Expert patterns for order processing, shipping coordination, and returns management.

## Order Lifecycle Management

### Complete Order Workflow
```
┌─────────────────────────────────────────────────────────────┐
│                   ORDER LIFECYCLE                            │
└─────────────────────────────────────────────────────────────┘

1. ORDER PLACED
   ├─ Customer submits order
   ├─ Payment authorization requested
   └─ Order confirmation email sent

2. PAYMENT PROCESSING
   ├─ Payment gateway processes
   ├─ Fraud screening
   ├─ If approved → PAID status
   └─ If declined → ON_HOLD status

3. ORDER VALIDATION
   ├─ Inventory check
   ├─ Address validation
   ├─ Shipping method confirmation
   └─ If issues → ON_HOLD for manual review

4. FULFILLMENT
   ├─ Pick items from warehouse
   ├─ Pack order
   ├─ Generate shipping label
   ├─ Scan tracking number
   └─ Status → SHIPPED

5. SHIPMENT
   ├─ Carrier picks up package
   ├─ In transit tracking updates
   ├─ Delivery attempted
   └─ Status → DELIVERED

6. POST-DELIVERY
   ├─ Delivery confirmation email
   ├─ Review request (after 3-7 days)
   ├─ Return window monitoring (30 days)
   └─ Status → COMPLETED
```

### Order States and Transitions
```javascript
const orderStateMachine = {
  PENDING: {
    description: 'Order received, awaiting payment',
    allowed_transitions: ['PAID', 'CANCELLED', 'ON_HOLD'],
    actions: ['authorize_payment', 'send_confirmation_email']
  },

  PAID: {
    description: 'Payment captured successfully',
    allowed_transitions: ['PROCESSING', 'CANCELLED', 'REFUNDED', 'ON_HOLD'],
    actions: ['reserve_inventory', 'notify_warehouse', 'send_payment_confirmation']
  },

  PROCESSING: {
    description: 'Order being prepared for shipment',
    allowed_transitions: ['SHIPPED', 'ON_HOLD', 'CANCELLED'],
    actions: ['pick_items', 'pack_order', 'generate_label', 'quality_check']
  },

  SHIPPED: {
    description: 'Package in transit to customer',
    allowed_transitions: ['DELIVERED', 'RETURNED_TO_SENDER', 'LOST'],
    actions: ['send_shipping_notification', 'track_shipment', 'update_eta']
  },

  DELIVERED: {
    description: 'Customer received package',
    allowed_transitions: ['COMPLETED', 'RETURN_REQUESTED'],
    actions: ['send_delivery_confirmation', 'request_review', 'monitor_return_window']
  },

  COMPLETED: {
    description: 'Order fulfilled successfully, past return window',
    allowed_transitions: [],
    actions: ['archive_order', 'update_clv']
  },

  // Exception states
  ON_HOLD: {
    description: 'Issue requiring manual review',
    reasons: ['payment_failed', 'fraud_suspected', 'address_invalid', 'out_of_stock'],
    allowed_transitions: ['PAID', 'PROCESSING', 'CANCELLED'],
    actions: ['notify_customer', 'flag_for_review', 'request_additional_info']
  },

  CANCELLED: {
    description: 'Order cancelled before shipment',
    allowed_transitions: ['REFUNDED'],
    actions: ['release_inventory', 'refund_payment', 'send_cancellation_email']
  },

  REFUNDED: {
    description: 'Payment returned to customer',
    allowed_transitions: [],
    actions: ['process_refund', 'update_inventory', 'send_refund_confirmation']
  },

  RETURN_REQUESTED: {
    description: 'Customer initiated return',
    allowed_transitions: ['RETURNED', 'RETURN_DENIED'],
    actions: ['issue_rma', 'send_return_label', 'track_return_shipment']
  }
};
```

## Shipping Coordination

### Carrier Selection Matrix
```python
def select_optimal_carrier(order):
    """
    Select best carrier based on weight, destination, speed, and cost
    """

    weight = order['weight_lbs']
    destination = order['shipping_address']
    service_level = order['shipping_method']
    value = order['total_value']

    # Domestic US shipping
    if destination['country'] == 'US':
        # Lightweight packages
        if weight <= 1:
            if service_level == 'standard':
                return {'carrier': 'USPS', 'service': 'First Class Package'}
            elif service_level == 'express':
                return {'carrier': 'USPS', 'service': 'Priority Mail Express'}

        # Standard packages
        elif weight <= 5:
            if service_level == 'standard':
                return {'carrier': 'USPS', 'service': 'Priority Mail'}
            elif service_level == 'express':
                return {'carrier': 'FedEx', 'service': '2Day'}

        # Heavy packages
        elif weight > 5:
            if service_level == 'standard':
                return {'carrier': 'UPS', 'service': 'Ground'}
            elif service_level == 'express':
                return {'carrier': 'FedEx', 'service': 'Standard Overnight'}

    # International shipping
    else:
        if weight <= 4:
            return {'carrier': 'USPS', 'service': 'Priority Mail International'}
        else:
            if service_level == 'express':
                return {'carrier': 'DHL', 'service': 'Express Worldwide'}
            else:
                return {'carrier': 'UPS', 'service': 'Worldwide Expedited'}

    # High-value insurance consideration
    if value > 500:
        return {'carrier': 'FedEx', 'service': 'Priority Overnight', 'insurance': value}

    # Default fallback
    return {'carrier': 'UPS', 'service': 'Ground'}
```

### Shipping Rate Calculation
```python
def calculate_shipping_rate(weight, dimensions, origin_zip, dest_zip, service):
    """
    Calculate shipping cost

    Factors:
    - Weight
    - Dimensional weight (for large, light items)
    - Distance (zone)
    - Service level
    - Additional services (signature, insurance)
    """

    # Dimensional weight
    dim_weight = (dimensions['length'] * dimensions['width'] * dimensions['height']) / 166
    billable_weight = max(weight, dim_weight)

    # Zone determination
    zone = get_shipping_zone(origin_zip, dest_zip)

    # Base rate (example rates)
    rate_table = {
        ('USPS', 'First Class', 1): 4.50,
        ('USPS', 'Priority', 3): 9.95,
        ('UPS', 'Ground', 5): 14.50,
        ('FedEx', '2Day', 5): 24.95,
        # ... more rates
    }

    # Get base rate
    rate_key = (service['carrier'], service['service'], zone)
    base_rate = rate_table.get(rate_key, 0)

    # Weight adjustments
    if billable_weight > 1:
        additional_lbs = billable_weight - 1
        base_rate += additional_lbs * 0.50  # $0.50 per additional lb

    # Additional services
    if service.get('signature_required'):
        base_rate += 3.50
    if service.get('insurance'):
        insurance_cost = (service['insurance'] / 100) * 1.00  # $1 per $100 value
        base_rate += max(1.00, insurance_cost)

    return round(base_rate, 2)
```

### Packaging Guidelines
```javascript
const packagingStandards = {
  box_selection: {
    small: {size: '8x6x4', weight_limit: 5, items: '1-2 small items'},
    medium: {size: '12x10x6', weight_limit: 15, items: '2-5 items'},
    large: {size: '18x14x8', weight_limit: 30, items: '5-10 items'},
    extra_large: {size: '24x18x12', weight_limit: 50, items: '10+ items'}
  },

  materials: {
    boxes: 'Corrugated cardboard, 200lb test minimum',
    padding: 'Bubble wrap, air pillows, or packing peanuts',
    tape: '2" wide packing tape, water-activated preferred',
    labels: 'Thermal labels 4x6 for shipping, 2x1 for SKU'
  },

  packing_process: [
    '1. Select appropriate box size',
    '2. Add 2" padding to bottom',
    '3. Place heaviest items at bottom',
    '4. Fill voids with padding (no shifting)',
    '5. Add 2" padding to top',
    '6. Seal with 3 strips of tape (H-pattern)',
    '7. Attach shipping label to largest face',
    '8. Add fragile stickers if needed',
    '9. Scan barcode to confirm correct item',
    '10. Weigh package and verify'
  ],

  quality_checks: {
    shake_test: 'No internal movement when shaken',
    drop_test: 'Can withstand 2ft drop (fragile: 1ft)',
    tape_coverage: 'All seams fully taped',
    label_placement: 'Flat surface, no overlap with seams',
    no_old_labels: 'All previous labels removed/covered'
  }
};
```

## Tracking and Notifications

### Tracking Status Updates
```python
def sync_tracking_status():
    """
    Poll carrier APIs for tracking updates and notify customers
    """

    shipments = get_active_shipments()

    for shipment in shipments:
        # Get latest tracking info from carrier
        tracking_data = carrier_api_track(shipment['carrier'], shipment['tracking_number'])

        # Check for status change
        if tracking_data['status'] != shipment['last_known_status']:
            # Update database
            update_shipment_status(shipment['id'], tracking_data['status'])

            # Customer notification logic
            if tracking_data['status'] == 'out_for_delivery':
                send_notification(shipment['customer_email'], 'delivery_today',
                    {
                        'tracking_number': shipment['tracking_number'],
                        'estimated_delivery': tracking_data['estimated_delivery']
                    })

            elif tracking_data['status'] == 'delivered':
                send_notification(shipment['customer_email'], 'delivered',
                    {
                        'delivery_time': tracking_data['delivery_time'],
                        'signed_by': tracking_data['signed_by'],
                        'order_number': shipment['order_number']
                    })

            elif tracking_data['status'] in ['exception', 'failed_delivery']:
                send_notification(shipment['customer_email'], 'delivery_exception',
                    {
                        'issue': tracking_data['exception_description'],
                        'next_attempt': tracking_data['next_attempt_date']
                    })

                # Internal alert for customer service
                alert_customer_service(shipment['id'], tracking_data['exception_description'])
```

### Email Notification Templates
```python
email_templates = {
    'order_confirmation': {
        'subject': 'Order #{order_number} Confirmed - Thank You!',
        'trigger': 'order_placed',
        'content': '''
            Hi {customer_name},

            Thank you for your order! We've received it and will process it shortly.

            ORDER DETAILS:
            Order Number: #{order_number}
            Order Date: {order_date}
            Order Total: ${order_total}

            ITEMS:
            {line_items}

            SHIPPING ADDRESS:
            {shipping_address}

            We'll send you another email when your order ships with tracking information.

            Questions? Reply to this email or call us at {support_phone}.

            Thanks for shopping with us!
            {store_name}
        '''
    },

    'shipment_notification': {
        'subject': 'Your Order #{order_number} Has Shipped! 📦',
        'trigger': 'order_shipped',
        'content': '''
            Great news! Your order is on its way.

            TRACKING INFO:
            Carrier: {carrier}
            Tracking Number: {tracking_number}
            Track your package: {tracking_url}

            Estimated Delivery: {estimated_delivery}

            WHAT'S IN YOUR PACKAGE:
            {line_items}

            Delivery Address:
            {shipping_address}

            If you won't be home, you can sign up for delivery alerts or request the package be held at a {carrier} location.

            Thanks!
            {store_name}
        '''
    },

    'delivery_confirmation': {
        'subject': 'Your Order Has Been Delivered! ✅',
        'trigger': 'order_delivered',
        'content': '''
            Your order #{order_number} was delivered!

            Delivered: {delivery_date} at {delivery_time}
            Location: {delivery_location}

            We hope you love your purchase! If you have a moment, we'd appreciate your feedback:
            {review_link}

            Need help with your order? Our team is here:
            Email: {support_email}
            Phone: {support_phone}

            Thanks for choosing {store_name}!
        '''
    }
}
```

## Returns Management

### Return Eligibility Check
```python
def check_return_eligibility(order_id, items_to_return, reason):
    """
    Determine if return request meets policy requirements
    """

    order = get_order(order_id)
    today = datetime.now()
    days_since_delivery = (today - order['delivered_date']).days

    eligibility = {
        'eligible': True,
        'issues': [],
        'rma_number': None
    }

    # Check return window (typically 30 days)
    if days_since_delivery > 30:
        eligibility['eligible'] = False
        eligibility['issues'].append(f'Return window expired ({days_since_delivery} days since delivery, limit is 30)')

    # Check for final sale items
    for item in items_to_return:
        product = get_product(item['sku'])
        if product.get('final_sale'):
            eligibility['eligible'] = False
            eligibility['issues'].append(f'{item["name"]} is final sale and cannot be returned')

    # Check for valid reason
    valid_reasons = ['defective', 'wrong_item', 'not_as_described', 'changed_mind', 'too_big', 'too_small']
    if reason not in valid_reasons:
        eligibility['eligible'] = False
        eligibility['issues'].append(f'Invalid return reason: {reason}')

    # Check for used/opened items (reason dependent)
    if reason == 'changed_mind':
        for item in items_to_return:
            if item.get('opened') or item.get('used'):
                eligibility['eligible'] = False
                eligibility['issues'].append(f'{item["name"]} has been opened/used and cannot be returned for "changed mind"')

    # Generate RMA if eligible
    if eligibility['eligible']:
        rma_number = f"RMA-{order_id}-{int(today.timestamp())}"
        eligibility['rma_number'] = rma_number

        # Create return label
        create_return_label(order, rma_number)

    return eligibility
```

### Return Process Workflow
```
┌─────────────────────────────────────────────────────────────┐
│                   RETURN WORKFLOW                            │
└─────────────────────────────────────────────────────────────┘

1. RETURN REQUESTED
   ├─ Customer initiates return
   ├─ Check eligibility
   ├─ If eligible → Issue RMA number
   └─ If ineligible → Notify customer with reason

2. RMA ISSUED
   ├─ Generate return shipping label
   ├─ Email label to customer
   ├─ Provide return instructions
   └─ Track return shipment

3. RETURN IN TRANSIT
   ├─ Monitor tracking
   ├─ Update customer on progress
   └─ Alert receiving team

4. RETURN RECEIVED
   ├─ Scan RMA number
   ├─ Inspect items:
   │  ├─ Check condition
   │  ├─ Verify items match RMA
   │  └─ Document any issues
   └─ Update return status

5. INSPECTION COMPLETE
   ├─ If accepted:
   │  ├─ Process refund
   │  ├─ Restock inventory (if sellable)
   │  └─ Email refund confirmation
   ├─ If rejected:
   │  ├─ Document rejection reason
   │  ├─ Offer to ship back (at customer cost)
   │  └─ Email explanation
   └─ If exchange requested:
      ├─ Ship replacement item
      └─ Process as new order

6. REFUND PROCESSED
   ├─ Refund to original payment method
   ├─ Processing time: 5-10 business days
   └─ Customer receives confirmation
```

### Refund Calculation
```python
def calculate_refund_amount(return_items, original_order, reason):
    """
    Calculate refund amount based on items and reason
    """

    subtotal = sum(item['price'] * item['quantity'] for item in return_items)

    # Deductions
    restocking_fee = 0
    shipping_refund = 0

    # Restocking fee (15% for "changed mind", 0% for defective/wrong item)
    if reason == 'changed_mind':
        restocking_fee = subtotal * 0.15

    # Shipping refund (only if wrong item or defective)
    if reason in ['wrong_item', 'defective', 'not_as_described']:
        shipping_refund = original_order['shipping_cost']

    # Calculate final refund
    refund_amount = subtotal - restocking_fee + shipping_refund

    # Round to 2 decimals
    refund_amount = round(refund_amount, 2)

    return {
        'refund_amount': refund_amount,
        'breakdown': {
            'items_subtotal': subtotal,
            'restocking_fee': restocking_fee,
            'shipping_refund': shipping_refund
        },
        'refund_to': original_order['payment_method'],
        'processing_time': '5-10 business days'
    }
```

## Fulfillment Metrics

### Key Performance Indicators
```python
fulfillment_kpis = {
    'order_accuracy': {
        'formula': '(correct_orders / total_orders) × 100',
        'target': '99.5% or higher',
        'definition': 'Orders with correct items, quantities, and no damage'
    },

    'time_to_ship': {
        'formula': 'Average hours from order paid to shipped status',
        'target': '<24 hours for standard, <4 hours for rush',
        'factors': ['order complexity', 'time of day', 'staffing']
    },

    'perfect_order_rate': {
        'formula': '(perfect_orders / total_orders) × 100',
        'target': '95% or higher',
        'perfect_order': 'Correct + On time + Undamaged + Correct docs'
    },

    'carrier_performance': {
        'on_time_delivery': '(delivered_on_time / total_deliveries) × 100',
        'target': '95% or higher',
        'damage_rate': '(damaged_shipments / total_shipments) × 100',
        'target_damage': '<1%'
    },

    'return_rate': {
        'formula': '(returns / total_orders) × 100',
        'target': '<10% (varies by category)',
        'fashion_typical': '20-30%',
        'electronics_typical': '5-10%'
    },

    'cost_per_shipment': {
        'formula': 'total_fulfillment_costs / total_shipments',
        'includes': 'Picking + packing + materials + labor + shipping',
        'target': 'Varies by AOV, typically 15-20% of order value'
    }
}
```

### Operational Excellence Practices
```javascript
const best_practices = {
  pick_accuracy: [
    'Barcode scanning (required for each item)',
    'Pick-to-light systems for high volume',
    'Double-check high-value orders',
    'Batch picking for efficiency',
    'Zone picking for large warehouses'
  ],

  pack_station_setup: [
    'Multiple box sizes readily available',
    'Padding materials within reach',
    'Scale integrated with system',
    'Label printer at each station',
    'Packing slip auto-generation',
    'Standard work instructions posted'
  ],

  quality_control: [
    'Random inspection (5-10% of orders)',
    '100% inspection for first 2 weeks of new pickers',
    'Photo documentation for high-value items',
    'Weight verification (flag if >10% variance)',
    'Address validation before label generation'
  ],

  continuous_improvement: [
    'Daily huddles to discuss issues',
    'Weekly metrics review',
    'Root cause analysis for errors',
    'Standard operating procedures (SOPs)',
    'Cross-training for flexibility',
    'Automation where ROI justifies'
  ]
};
```

This skill provides comprehensive order fulfillment patterns for e-commerce operations.
