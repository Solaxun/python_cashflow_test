from do_not_modify import tests

## utilize these amounts to meet funding needs
FUNDING_SOURCES = {
	'fedfunds': {
		'available': 25000,
		'cost': 0.006,
		'increment': 500
	},

	'fhlb': {
		'available': 35000,
		'cost': 0.009,
		'increment': 95
	},

	'brokered3m': {
		'available': 25000,
		'cost': 0.013,
		'increment': 55
	},

	'brokered5m': {
		'available': 27000,
		'cost': 0.018,
		'increment': 65
	},

	'debt': {
		'available': 30000,
		'cost': 0.025,
		'increment': 25
	}
}
## Starting balance sheet. Update to reflect changes from cash
## inflows/outflows and related uses of funding sources.
BALANCE_SHEET = {
	'cash': 50695,
	'loans': 122860,
  'checking': 25000,
	'CDs': 57500,
	'savings': 85000,
	'fedfunds': 0,
  'fhlb':0,
  'brokered3m':0,
  'brokered5m':0,
  'debt':0
}

## cash inflows(+) and outflows (-)
CASH_FLOWS = open('do_not_modify/cashflows.txt').read()

################################
## IMPLEMENTATION - START HERE
################################
def parse_cashflows(raw_cashflows):
  """
  Parse the raw text input in `cashflows.txt` into a list
  of cashflow events which can be handled by `process_cashflows`.
  
  @return: 
  [['4/21/2017 7:12:19',-521.38,'CDs']]
  """
  return []

def process_cashflows(parsed_cashflows,funding_sources,balance_sheet):
  """
  @params:

  @parsed_cashflows:    [[string|date, float, string]]
  @funding_sources:     {string: {string:float}}
  @balance_sheet:       {string: float}

  @return:

  (@balance_sheet, @funding_sources)
  """
  return {},{}