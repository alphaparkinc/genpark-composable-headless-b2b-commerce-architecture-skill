from client import ComposableHeadlessB2bCommerceArchitectureClient

def main():
    client = ComposableHeadlessB2bCommerceArchitectureClient()
    res = client.build_b2b_punchout_quote('ORG_BOSCH_GLOBAL', 'director')
    print('Quote: ' + res['quote_id'] + ' for ' + res['buyer_org'])
    print('cXML Punchout: ' + str(res['cxml_punchout_supported']) + ' | Approval Limit: EUR ' + str(res['automated_approval_threshold_eur']))
    print('Warehouses: ' + ', '.join(res['split_shipment_warehouse_routing']))

if __name__ == '__main__':
    main()
