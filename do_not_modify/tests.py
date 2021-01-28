import main

def test_ending_funding_sources(funding_sources):
    funding_sources = {k:v for k,v in funding_sources.items() if v['available'] > 0}
    assert(len(funding_sources) == 1 and funding_sources['debt']['available'] == 1325)

def test_ending_balance_sheet(balance_sheet):
    expected =  {
      'cash': 31027.82,
      'loans': 155973.48,
      'checking': 11382.22,
      'CDs': 3918.89,
      'savings': 24970.19,
      'fedfunds': 25000,
      'fhlb': 35000,
      'brokered3m': 25000,
      'brokered5m': 27000,
      'debt': 28675
      }
    assert(expected == {k:round(v,2) for k,v in balance_sheet.items()})

def run_tests(bs,fs):
  try:
    test_ending_balance_sheet(bs)
    test_ending_funding_sources(fs)
  except AssertionError as e:
    print('Tests Failed.')
    raise e
    return
  print('All Tests Pass!')

run_tests(*main.process_cashflows(main.parse_cashflows(main.CASH_FLOWS),
                                  main.FUNDING_SOURCES,
                                  main.BALANCE_SHEET))
  