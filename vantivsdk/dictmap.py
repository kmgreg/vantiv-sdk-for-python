# -*- coding: utf-8 -*-l
# Copyright (c) 2017 Vantiv eCommerce
#
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation
# files (the "Software"), to deal in the Software without
# restriction, including without limitation the rights to use,
# copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following
# conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.
#
from __future__ import unicode_literals

# The following dict is automatically generated by tools/postGeneration.py, Please DO NOT manually change it.

txns_dict = {'accountUpdate': {'cardOrToken': 'cardOrToken',
                 'customerId': '',
                 'id': '',
                 'orderId': '',
                 'reportGroup': ''},
'activate': {'amount': '',
            'card': 'giftCardCardType',
            'customerId': '',
            'id': '',
            'orderId': '',
            'orderSource': '',
            'reportGroup': '',
            'virtualGiftCard': 'virtualGiftCardType'},
'activateReversal': {'card': 'giftCardCardType',
                    'customerId': '',
                    'id': '',
                    'litleTxnId': '',
                    'originalAmount': '',
                    'originalRefCode': '',
                    'originalSequenceNumber': '',
                    'originalSystemTraceId': '',
                    'originalTxnTime': '',
                    'reportGroup': '',
                    'virtualGiftCardBin': ''},
'authReversal': {'actionReason': '',
                'amount': '',
                'customerId': '',
                'id': '',
                'litleTxnId': '',
                'payPalNotes': '',
                'reportGroup': '',
                'surchargeAmount': ''},
'authorization': {'advancedFraudChecks': 'advancedFraudChecksType',
                 'allowPartialAuth': '',
                 'amexAggregatorData': 'amexAggregatorData',
                 'amount': '',
                 'applepay': 'applepayType',
                 'billMeLaterRequest': 'billMeLaterRequest',
                 'billToAddress': 'billToAddress',
                 'card': 'cardType',
                 'cardholderAuthentication': 'fraudCheckType',
                 'customBilling': 'customBilling',
                 'customerId': '',
                 'customerInfo': 'customerInfo',
                 'debtRepayment': '',
                 'enhancedData': 'enhancedData',
                 'filtering': 'filteringType',
                 'fraudFilterOverride': '',
                 'healthcareIIAS': 'healthcareIIAS',
                 'id': '',
                 'litleTxnId': '',
                 'merchantData': 'merchantDataType',
                 'mpos': 'mposType',
                 'orderId': '',
                 'orderSource': '',
                 'originalNetworkTransactionId': '',
                 'originalTransactionAmount': '',
                 'paypage': 'cardPaypageType',
                 'paypal': 'payPal',
                 'pos': 'pos',
                 'processingInstructions': 'processingInstructions',
                 'processingType': '',
                 'recurringRequest': 'recurringRequestType',
                 'recyclingRequest': 'recyclingRequestType',
                 'reportGroup': '',
                 'secondaryAmount': '',
                 'shipToAddress': 'shipToAddress',
                 'surchargeAmount': '',
                 'taxType': '',
                 'token': 'cardTokenType',
                 'wallet': 'wallet'},
'balanceInquiry': {'card': 'giftCardCardType',
                  'customerId': '',
                  'id': '',
                  'orderId': '',
                  'orderSource': '',
                  'reportGroup': ''},
'cancelSubscription': {'subscriptionId': ''},
'capture': {'amount': '',
           'customBilling': 'customBilling',
           'customerId': '',
           'enhancedData': 'enhancedData',
           'id': '',
           'litleTxnId': '',
           'partial': '',
           'payPalNotes': '',
           'payPalOrderComplete': '',
           'pin': '',
           'processingInstructions': 'processingInstructions',
           'reportGroup': '',
           'surchargeAmount': ''},
'captureGivenAuth': {'amexAggregatorData': 'amexAggregatorData',
                    'amount': '',
                    'authInformation': 'authInformation',
                    'billMeLaterRequest': 'billMeLaterRequest',
                    'billToAddress': 'billToAddress',
                    'card': 'cardType',
                    'customBilling': 'customBilling',
                    'customerId': '',
                    'debtRepayment': '',
                    'enhancedData': 'enhancedData',
                    'id': '',
                    'merchantData': 'merchantDataType',
                    'mpos': 'mposType',
                    'orderId': '',
                    'orderSource': '',
                    'originalNetworkTransactionId': '',
                    'originalTransactionAmount': '',
                    'paypage': 'cardPaypageType',
                    'pos': 'pos',
                    'processingInstructions': 'processingInstructions',
                    'processingType': '',
                    'reportGroup': '',
                    'secondaryAmount': '',
                    'shipToAddress': 'shipToAddress',
                    'surchargeAmount': '',
                    'taxType': '',
                    'token': 'cardTokenType'},
'createPlan': {'active': '',
              'amount': '',
              'description': '',
              'intervalType': '',
              'name': '',
              'numberOfPayments': '',
              'planCode': '',
              'trialIntervalType': '',
              'trialNumberOfIntervals': ''},
'credit': {'actionReason': '',
          'amexAggregatorData': 'amexAggregatorData',
          'amount': '',
          'billMeLaterRequest': 'billMeLaterRequest',
          'billToAddress': 'billToAddress',
          'card': 'cardType',
          'customBilling': 'customBilling',
          'customerId': '',
          'enhancedData': 'enhancedData',
          'id': '',
          'litleTxnId': '',
          'merchantData': 'merchantDataType',
          'mpos': 'mposType',
          'orderId': '',
          'orderSource': '',
          'payPalNotes': '',
          'paypage': 'cardPaypageType',
          'paypal': 'payPal',
          'pin': '',
          'pos': 'pos',
          'processingInstructions': 'processingInstructions',
          'reportGroup': '',
          'secondaryAmount': '',
          'surchargeAmount': '',
          'taxType': '',
          'token': 'cardTokenType'},
'deactivate': {'card': 'giftCardCardType',
              'customerId': '',
              'id': '',
              'orderId': '',
              'orderSource': '',
              'reportGroup': ''},
'deactivateReversal': {'card': 'giftCardCardType',
                      'customerId': '',
                      'id': '',
                      'litleTxnId': '',
                      'originalRefCode': '',
                      'originalSequenceNumber': '',
                      'originalSystemTraceId': '',
                      'originalTxnTime': '',
                      'reportGroup': ''},
'depositReversal': {'card': 'giftCardCardType',
                   'customerId': '',
                   'id': '',
                   'litleTxnId': '',
                   'originalAmount': '',
                   'originalRefCode': '',
                   'originalSequenceNumber': '',
                   'originalSystemTraceId': '',
                   'originalTxnTime': '',
                   'reportGroup': ''},
'echeckCredit': {'amount': '',
                'billToAddress': 'billToAddress',
                'customBilling': 'customBilling',
                'customIdentifier': '',
                'customerId': '',
                'echeckOrEcheckToken': 'echeckOrEcheckToken',
                'id': '',
                'litleTxnId': '',
                'merchantData': 'merchantDataType',
                'orderId': '',
                'orderSource': '',
                'reportGroup': '',
                'secondaryAmount': ''},
'echeckPreNoteCredit': {'billToAddress': 'billToAddress',
                       'customerId': '',
                       'echeck': 'echeck',
                       'id': '',
                       'merchantData': 'merchantDataType',
                       'orderId': '',
                       'orderSource': '',
                       'reportGroup': ''},
'echeckPreNoteSale': {'billToAddress': 'billToAddress',
                     'customerId': '',
                     'echeck': 'echeck',
                     'id': '',
                     'merchantData': 'merchantDataType',
                     'orderId': '',
                     'orderSource': '',
                     'reportGroup': ''},
'echeckRedeposit': {'customIdentifier': '',
                   'customerId': '',
                   'echeckOrEcheckToken': 'echeckOrEcheckToken',
                   'id': '',
                   'litleTxnId': '',
                   'merchantData': 'merchantDataType',
                   'reportGroup': ''},
'echeckSale': {'amount': '',
              'billToAddress': 'billToAddress',
              'customBilling': 'customBilling',
              'customIdentifier': '',
              'customerId': '',
              'echeckOrEcheckToken': 'echeckOrEcheckToken',
              'id': '',
              'litleTxnId': '',
              'merchantData': 'merchantDataType',
              'orderId': '',
              'orderSource': '',
              'reportGroup': '',
              'secondaryAmount': '',
              'shipToAddress': 'shipToAddress',
              'verify': ''},
'echeckVerification': {'amount': '',
                      'billToAddress': 'billToAddress',
                      'customerId': '',
                      'echeckOrEcheckToken': 'echeckOrEcheckToken',
                      'id': '',
                      'merchantData': 'merchantDataType',
                      'orderId': '',
                      'orderSource': '',
                      'reportGroup': ''},
'echeckVoid': {'customerId': '',
              'id': '',
              'litleTxnId': '',
              'reportGroup': ''},
'forceCapture': {'amexAggregatorData': 'amexAggregatorData',
                'amount': '',
                'billToAddress': 'billToAddress',
                'card': 'cardType',
                'customBilling': 'customBilling',
                'customerId': '',
                'debtRepayment': '',
                'enhancedData': 'enhancedData',
                'id': '',
                'merchantData': 'merchantDataType',
                'mpos': 'mposType',
                'orderId': '',
                'orderSource': '',
                'paypage': 'cardPaypageType',
                'pos': 'pos',
                'processingInstructions': 'processingInstructions',
                'processingType': '',
                'reportGroup': '',
                'secondaryAmount': '',
                'surchargeAmount': '',
                'taxType': '',
                'token': 'cardTokenType'},
'fraudCheck': {'advancedFraudChecks': 'advancedFraudChecksType',
              'amount': '',
              'billToAddress': 'billToAddress',
              'customerId': '',
              'id': '',
              'reportGroup': '',
              'shipToAddress': 'shipToAddress'},
'fundingInstructionVoid': {'customerId': '',
                          'id': '',
                          'litleTxnId': '',
                          'reportGroup': ''},
'giftCardAuthReversal': {'card': 'giftCardCardType',
                        'customerId': '',
                        'id': '',
                        'litleTxnId': '',
                        'originalAmount': '',
                        'originalRefCode': '',
                        'originalSequenceNumber': '',
                        'originalSystemTraceId': '',
                        'originalTxnTime': '',
                        'reportGroup': ''},
'giftCardCapture': {'captureAmount': '',
                   'card': 'giftCardCardType',
                   'customerId': '',
                   'id': '',
                   'litleTxnId': '',
                   'originalAmount': '',
                   'originalRefCode': '',
                   'originalTxnTime': '',
                   'partial': '',
                   'reportGroup': ''},
'giftCardCredit': {'card': 'giftCardCardType',
                  'creditAmount': '',
                  'customerId': '',
                  'id': '',
                  'litleTxnId': '',
                  'orderId': '',
                  'orderSource': '',
                  'reportGroup': ''},
'load': {'amount': '',
        'card': 'giftCardCardType',
        'customerId': '',
        'id': '',
        'orderId': '',
        'orderSource': '',
        'reportGroup': ''},
'loadReversal': {'card': 'giftCardCardType',
                'customerId': '',
                'id': '',
                'litleTxnId': '',
                'originalAmount': '',
                'originalRefCode': '',
                'originalSequenceNumber': '',
                'originalSystemTraceId': '',
                'originalTxnTime': '',
                'reportGroup': ''},
'payFacCredit': {'amount': '',
                'customerId': '',
                'fundingSubmerchantId': '',
                'fundsTransferId': '',
                'id': '',
                'reportGroup': ''},
'payFacDebit': {'amount': '',
               'customerId': '',
               'fundingSubmerchantId': '',
               'fundsTransferId': '',
               'id': '',
               'reportGroup': ''},
'physicalCheckCredit': {'amount': '',
                       'customerId': '',
                       'fundingSubmerchantId': '',
                       'fundsTransferId': '',
                       'id': '',
                       'reportGroup': ''},
'physicalCheckDebit': {'amount': '',
                      'customerId': '',
                      'fundingSubmerchantId': '',
                      'fundsTransferId': '',
                      'id': '',
                      'reportGroup': ''},
'queryTransaction': {'customerId': '',
                    'id': '',
                    'origActionType': '',
                    'origId': '',
                    'origLitleTxnId': '',
                    'reportGroup': ''},
'refundReversal': {'card': 'giftCardCardType',
                  'customerId': '',
                  'id': '',
                  'litleTxnId': '',
                  'originalAmount': '',
                  'originalRefCode': '',
                  'originalSequenceNumber': '',
                  'originalSystemTraceId': '',
                  'originalTxnTime': '',
                  'reportGroup': ''},
'registerTokenRequest': {'accountNumber': '',
                        'applepay': 'applepayType',
                        'cardValidationNum': '',
                        'customerId': '',
                        'echeckForToken': 'echeckForTokenType',
                        'id': '',
                        'mpos': 'mposType',
                        'orderId': '',
                        'paypageRegistrationId': '',
                        'reportGroup': ''},
'reserveCredit': {'amount': '',
                 'customerId': '',
                 'fundingSubmerchantId': '',
                 'fundsTransferId': '',
                 'id': '',
                 'reportGroup': ''},
'reserveDebit': {'amount': '',
                'customerId': '',
                'fundingSubmerchantId': '',
                'fundsTransferId': '',
                'id': '',
                'reportGroup': ''},
'sale': {'advancedFraudChecks': 'advancedFraudChecksType',
        'allowPartialAuth': '',
        'amexAggregatorData': 'amexAggregatorData',
        'amount': '',
        'applepay': 'applepayType',
        'billMeLaterRequest': 'billMeLaterRequest',
        'billToAddress': 'billToAddress',
        'card': 'cardType',
        'cardholderAuthentication': 'fraudCheckType',
        'customBilling': 'customBilling',
        'customerId': '',
        'customerInfo': 'customerInfo',
        'debtRepayment': '',
        'enhancedData': 'enhancedData',
        'filtering': 'filteringType',
        'fraudCheck': 'fraudCheckType',
        'fraudFilterOverride': '',
        'giropay': 'giropayType',
        'healthcareIIAS': 'healthcareIIAS',
        'id': '',
        'ideal': 'idealType',
        'litleInternalRecurringRequest': 'litleInternalRecurringRequestType',
        'litleTxnId': '',
        'merchantData': 'merchantDataType',
        'mpos': 'mposType',
        'orderId': '',
        'orderSource': '',
        'originalNetworkTransactionId': '',
        'originalTransactionAmount': '',
        'payPalNotes': '',
        'payPalOrderComplete': '',
        'paypage': 'cardPaypageType',
        'paypal': 'payPal',
        'pos': 'pos',
        'processingInstructions': 'processingInstructions',
        'processingType': '',
        'recurringRequest': 'recurringRequestType',
        'recyclingRequest': 'recyclingRequestType',
        'reportGroup': '',
        'secondaryAmount': '',
        'sepaDirectDebit': 'sepaDirectDebitType',
        'shipToAddress': 'shipToAddress',
        'sofort': 'sofortType',
        'surchargeAmount': '',
        'taxType': '',
        'token': 'cardTokenType',
        'wallet': 'wallet'},
'serviceStatusRequest': {'customerId': '',
                        'id': '',
                        'pathId': '',
                        'reportGroup': '',
                        'serviceId': ''},
'submerchantCredit': {'accountInfo': 'echeckType',
                     'amount': '',
                     'customIdentifier': '',
                     'customerId': '',
                     'fundingSubmerchantId': '',
                     'fundsTransferId': '',
                     'id': '',
                     'reportGroup': '',
                     'submerchantName': ''},
'submerchantDebit': {'accountInfo': 'echeckType',
                    'amount': '',
                    'customIdentifier': '',
                    'customerId': '',
                    'fundingSubmerchantId': '',
                    'fundsTransferId': '',
                    'id': '',
                    'reportGroup': '',
                    'submerchantName': ''},
'unload': {'amount': '',
          'card': 'giftCardCardType',
          'customerId': '',
          'id': '',
          'orderId': '',
          'orderSource': '',
          'reportGroup': ''},
'unloadReversal': {'card': 'giftCardCardType',
                  'customerId': '',
                  'id': '',
                  'litleTxnId': '',
                  'originalAmount': '',
                  'originalRefCode': '',
                  'originalSequenceNumber': '',
                  'originalSystemTraceId': '',
                  'originalTxnTime': '',
                  'reportGroup': ''},
'updateCardValidationNumOnToken': {'cardValidationNum': '',
                                  'customerId': '',
                                  'id': '',
                                  'litleToken': '',
                                  'orderId': '',
                                  'reportGroup': ''},
'updatePlan': {'active': '', 'planCode': ''},
'updateSubscription': {'billToAddress': 'billToAddress',
                      'billingDate': '',
                      'card': 'cardType',
                      'createAddOn': 'createAddOnType',
                      'createDiscount': 'createDiscountType',
                      'deleteAddOn': 'deleteAddOnType',
                      'deleteDiscount': 'deleteDiscountType',
                      'paypage': 'cardPaypageType',
                      'planCode': '',
                      'subscriptionId': '',
                      'token': 'cardTokenType',
                      'updateAddOn': 'updateAddOnType',
                      'updateDiscount': 'updateDiscountType'},
'vendorCredit': {'accountInfo': 'echeckType',
                'amount': '',
                'customerId': '',
                'fundingSubmerchantId': '',
                'fundsTransferId': '',
                'id': '',
                'reportGroup': '',
                'vendorName': ''},
'vendorDebit': {'accountInfo': 'echeckType',
               'amount': '',
               'customerId': '',
               'fundingSubmerchantId': '',
               'fundsTransferId': '',
               'id': '',
               'reportGroup': '',
               'vendorName': ''},
'void': {'customerId': '',
        'id': '',
        'litleTxnId': '',
        'processingInstructions': 'processingInstructions',
        'reportGroup': ''}}

used_type_dict = {'advancedFraudChecksType': {'customAttribute1': '',
                           'customAttribute2': '',
                           'customAttribute3': '',
                           'customAttribute4': '',
                           'customAttribute5': '',
                           'threatMetrixSessionId': ''},
'advancedFraudResultsType': {'deviceReputationScore': '',
                            'deviceReviewStatus': '',
                            'triggeredRule': ''},
'amexAggregatorData': {'sellerId': '', 'sellerMerchantCategoryCode': ''},
'applepayHeaderType': {'applicationData': '',
                      'ephemeralPublicKey': '',
                      'publicKeyHash': '',
                      'transactionId': ''},
'applepayType': {'data': '',
                'header': 'applepayHeaderType',
                'signature': '',
                'version': ''},
'authInformation': {'authAmount': '',
                   'authCode': '',
                   'authDate': '',
                   'fraudResult': 'fraudResult'},
'billMeLaterRequest': {'authorizationSourcePlatform': '',
                      'bmlMerchantId': '',
                      'bmlProductType': 'bmlProductType',
                      'customerBillingAddressChanged': '',
                      'customerEmailChanged': '',
                      'customerPasswordChanged': '',
                      'customerPhoneChanged': '',
                      'itemCategoryCode': '',
                      'merchantPromotionalCode': '',
                      'preapprovalNumber': '',
                      'secretQuestionAnswer': '',
                      'secretQuestionCode': '',
                      'termsAndConditions': '',
                      'virtualAuthenticationKeyData': '',
                      'virtualAuthenticationKeyPresenceIndicator': ''},
'billToAddress': {'addressLine1': '',
                 'addressLine2': '',
                 'addressLine3': '',
                 'city': '',
                 'companyName': '',
                 'country': '',
                 'email': '',
                 'firstName': '',
                 'lastName': '',
                 'middleInitial': '',
                 'name': '',
                 'phone': '',
                 'state': '',
                 'zip': ''},
'bmlProductType': {},
'card': {'cardValidationNum': '',
        'expDate': '',
        'number': '',
        'pin': '',
        'track': '',
        'type': ''},
'cardPaypageType': {'cardValidationNum': '',
                   'expDate': '',
                   'paypageRegistrationId': '',
                   'type': ''},
'cardTokenType': {'cardValidationNum': '',
                 'checkoutId': '',
                 'expDate': '',
                 'litleToken': '',
                 'type': ''},
'cardType': {'cardValidationNum': '',
            'expDate': '',
            'number': '',
            'pin': '',
            'track': '',
            'type': ''},
'createAddOnType': {'addOnCode': '',
                   'amount': '',
                   'endDate': '',
                   'name': '',
                   'startDate': ''},
'createDiscountType': {'amount': '',
                      'discountCode': '',
                      'endDate': '',
                      'name': '',
                      'startDate': ''},
'customBilling': {'city': '', 'descriptor': '', 'phone': '', 'url': ''},
'customerInfo': {'customerCheckingAccount': '',
                'customerRegistrationDate': '',
                'customerSavingAccount': '',
                'customerType': '',
                'customerWorkTelephone': '',
                'dob': '',
                'employerName': '',
                'incomeAmount': '',
                'incomeCurrency': '',
                'residenceStatus': '',
                'ssn': '',
                'yearsAtEmployer': '',
                'yearsAtResidence': ''},
'deleteAddOnType': {'addOnCode': ''},
'deleteDiscountType': {'discountCode': ''},
'detailTax': {'cardAcceptorTaxId': '',
             'taxAmount': '',
             'taxIncludedInTotal': '',
             'taxRate': '',
             'taxTypeIdentifier': ''},
'echeck': {'accNum': '',
          'accType': '',
          'ccdPaymentInformation': '',
          'checkNum': '',
          'routingNum': ''},
'echeckForTokenType': {'accNum': '', 'routingNum': ''},
'echeckToken': {'accType': '',
               'checkNum': '',
               'litleToken': '',
               'routingNum': ''},
'echeckType': {'accNum': '',
              'accType': '',
              'ccdPaymentInformation': '',
              'checkNum': '',
              'routingNum': ''},
'enhancedData': {'customerReference': '',
                'deliveryType': '',
                'destinationCountryCode': '',
                'destinationPostalCode': '',
                'detailTax': 'detailTax',
                'discountAmount': '',
                'dutyAmount': '',
                'invoiceReferenceNumber': '',
                'lineItemData': 'lineItemData',
                'orderDate': '',
                'salesTax': '',
                'shipFromPostalCode': '',
                'shippingAmount': '',
                'taxExempt': ''},
'filteringType': {'chargeback': '', 'international': '', 'prepaid': ''},
'fraudCheckType': {'authenticatedByMerchant': '',
                  'authenticationTransactionId': '',
                  'authenticationValue': '',
                  'customerIpAddress': ''},
'fraudResult': {'advancedAVSResult': '',
               'advancedFraudResults': 'advancedFraudResultsType',
               'authenticationResult': '',
               'avsResult': '',
               'cardValidationResult': ''},
'giftCardCardType': {'cardValidationNum': '',
                    'expDate': '',
                    'number': '',
                    'pin': '',
                    'track': '',
                    'type': ''},
'giropayType': {'preferredLanguage': ''},
'healthcareAmounts': {'RxAmount': '',
                     'clinicOtherAmount': '',
                     'dentalAmount': '',
                     'totalHealthcareAmount': '',
                     'visionAmount': ''},
'healthcareIIAS': {'IIASFlag': '', 'healthcareAmounts': 'healthcareAmounts'},
'idealType': {'preferredLanguage': ''},
'lineItemData': {'commodityCode': '',
                'detailTax': 'detailTax',
                'itemDescription': '',
                'itemDiscountAmount': '',
                'itemSequenceNumber': '',
                'lineItemTotal': '',
                'lineItemTotalWithTax': '',
                'productCode': '',
                'quantity': '',
                'taxAmount': '',
                'unitCost': '',
                'unitOfMeasure': ''},
'litleInternalRecurringRequestType': {'finalPayment': '',
                                     'recurringTxnId': '',
                                     'subscriptionId': ''},
'merchantDataType': {'affiliate': '',
                    'campaign': '',
                    'merchantGroupingId': ''},
'mposType': {'encryptedTrack': '',
            'formatId': '',
            'ksn': '',
            'track1Status': '',
            'track2Status': ''},
'payPal': {'payerEmail': '', 'payerId': '', 'token': '', 'transactionId': ''},
'pos': {'capability': '',
       'cardholderId': '',
       'catLevel': '',
       'entryMode': '',
       'terminalId': ''},
'processingInstructions': {'bypassVelocityCheck': ''},
'recurringRequestType': {'subscription': 'recurringSubscriptionType'},
'recurringSubscriptionType': {'amount': '',
                             'createAddOn': 'createAddOnType',
                             'createDiscount': 'createDiscountType',
                             'numberOfPayments': '',
                             'planCode': '',
                             'startDate': ''},
'recyclingRequestType': {'recycleBy': '', 'recycleId': ''},
'sepaDirectDebitType': {'iban': '',
                       'mandateProvider': '',
                       'mandateReference': '',
                       'mandateSignatureDate': '',
                       'mandateUrl': '',
                       'preferredLanguage': '',
                       'sequenceType': ''},
'shipToAddress': {'addressLine1': '',
                 'addressLine2': '',
                 'addressLine3': '',
                 'city': '',
                 'companyName': '',
                 'country': '',
                 'email': '',
                 'firstName': '',
                 'lastName': '',
                 'middleInitial': '',
                 'name': '',
                 'phone': '',
                 'state': '',
                 'zip': ''},
'sofortType': {'preferredLanguage': ''},
'token': {'cardValidationNum': '',
         'checkoutId': '',
         'expDate': '',
         'litleToken': '',
         'type': ''},
'updateAddOnType': {'addOnCode': '',
                   'amount': '',
                   'endDate': '',
                   'name': '',
                   'startDate': ''},
'updateDiscountType': {'amount': '',
                      'discountCode': '',
                      'endDate': '',
                      'name': '',
                      'startDate': ''},
'virtualGiftCardType': {'accountNumberLength': '', 'giftCardBin': ''},
'wallet': {'walletSourceType': '', 'walletSourceTypeId': ''}}

abs_class_dict = {'echeckOrEcheckToken': ['echeck', 'echeckToken'], 'cardOrToken': ['card', 'token']}
