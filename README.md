## Objective
Process cash flows and ensure cash balances never fall below $20,000 by utilizing available funding sources.  For purposes of this exercise, you do not need to consider the maturity of such funding sources - the maturity is assumed to extend beyond the horizon of the exercise.  If implemented correctly, funding sources will always have enough availability to maintain appropriate cash balances.  For example,  there should not be a situation in which cash is below $20,000 and all funding sources have been depleted. 

Final results should show the balance sheet adjusted for the various cash flows and remediating funding actions taken, along with the remaining (if any) funding sources available.

## Instructions
Modify *only* the code in `main.py`, starting at line 56.  

Within the body of `process_cashflows` it is assumed that the *parameter* `parsed_cashflows` has been bound to the value returned by the *function* `parse_cashflows`. This requires implementing the *function* `parse_cashflows`, which will be called on `cashflows.txt` prior to invocation of `process_cashflows`. For example, the test cases will call `process_cashflows` as follows:

```python
process_cashflows(parse_cashflows('cashflows.txt'),FUNDING_SOURCES,BALANCE_SHEET)
```

The value returned from this function should be a tuple of the `BALANCE_SHEET` and `FUNDING_SOURCES` dictionaries after updating them for the cash flows in `cashflows.txt` and related funding actions taken to neutralize such flows.

#### The following constraints must be honored:
- Each funding source may be used up to it's available amount in increments specified by such source.
  - As an example, below `fedfunds` has $400 available, but may only be borrowed in increments of $50.  Therefore if a $90 shortfall in cash is present, you may only borrow $100 from this source, not $90.

- Balance Sheet cash must at all times remain at or above $20,000.  If a cash flow causes this amount to fall beneath the $20,000 limit, utilize vailable funding to maintain required cash levels.

- Always use the cheapest available funding source first.  Once that
source is exhausted, use the next cheapest source, etc.  You should always have enough funding availability to meet cash demands if the implementation is correct.   
 
## Simplified Example:
Below, we only have two funding sources available - fedfunds and fhlb.  Since fhlb is the cheaper funding source, we will always elect to use this source first.
``` python
## used to maintain cash levels
funding_sources = {
'fedfunds': {
  'available': 400,
  'cost': 0.010,
  'increment': 50
  },

'fhlb': {
  'available': 700,
  'cost': 0.0019,
  'increment': 10
  }
}

## starting balance sheet, adjust for cash flows and funding actions
balance_sheet = {
'cash': 20000,
'loans': 50000,
'checking': 10000,
'CDs': 55000,
'savings': 15000,
'fedfunds': 0,
'fhlb':0,
'brokered3m':0,
'brokered5m':0,
'debt':0
}

## cash flows to be processed (after parsing, e.g. output of `parse_cashflows`)
cash_flows = [
 ['4/21/2017 7:12:12', -995.34, 'Checking'],
 ['4/21/2017 7:12:13', 5145.92, 'Loan Repayment']
]
```
#### Cash Flow 1 - Checking Deposit Outflow of $995.34
The following actions are taken:

- The cheapest available source is fhlb, which may be borrowed up to it's capacity of $700, in whole increments of $10.  

- We borrow the full amount that's available ($700) leaving us with a remaining shortfall of ($995.34 - $700 = $295.34)

- The only remaining funding source is fedfunds, with a capacity of $400 which may be borrowed in whole increments of $50

- Borrow $300 of fed funds, neutralizing the remaining shortfall and leaving a small surplus of ($300 - $295.34 = $4.66)

- Balance sheet cash is updated to reflect this surplus, and is now ($20,000 + $4.66 = $20,004.66)

- Similarly, other balance sheet items are updated to reflect these funding activities: 
  - fedfunds increase from $0 to $300
  - fhlb increase from $0 to $700
  - checking deposits decrease from $10,000 to $9,004.66
 
- funding sources are updated to reflect the remaining available capacity:
  - fhlb available capacity is now $0, as the full $700 was used.
  - fedfunds remaining capacity is $100, as $300 was used.

#### Cash Flow 2 - Loan Repayment of $5,145.92. 
The following actions are taken: 

- Balance Sheet Cash increases to ($20,004.66 + $5,145.92 = $25,150.58)
- Balance Sheet Loans decrease by the repaid amount ($50,000 - $5,145.92 = $44,854.08)
- Funding sources are unmodified

## Expected Output

After applying both cash flows, and utilizing the appropriate funding sources, the final balance sheet and funding sources are as follows:

``` python
funding_sources = {
'fedfunds': {
  'available': 100,
  'cost': 0.010,
  'increment': 50
  },

'fhlb': {
  'available': 0,
  'cost': 0.0019,
  'increment': 10
  }
}

balance_sheet = {
'cash': 25150.58,
'loans': 44854.08,
'checking': 9004.66,
'CDs': 55000,
'savings': 15000,
'fedfunds': 300,
'fhlb':700,
'brokered3m':0,
'brokered5m':0,
'debt':0
}
```
Return these values in a tuple of (balance_sheet,funding_sources) from the `process_cashflows` function in `main.py`.  If implemented correctly, you will receive a message stating all of the tests have passed.

