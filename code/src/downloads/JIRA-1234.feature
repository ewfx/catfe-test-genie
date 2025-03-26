
Feature: SWIFT ISO Payment Processing Compliance
  Jira ID: JIRA-1234

  Description: As a payment operations manager, I want the system to process international payments according to the latest SWIFT ISO 20022 standards so that we ensure compliance with global payment regulations and avoid settlement delays with partner banks.

  Acceptance Criteria:
  The system must validate that payment messages include mandatory SWIFT ISO 20022 fields (e.g., debtor IBAN, creditor IBAN, amount, currency).
Reject payments with missing or invalid mandatory fields.
Process payments with valid SWIFT ISO 20022 fields within 10 seconds and send them to the partner bank.
Log all payment transactions, including validation failures, for audit purposes.
Notify the operations team if a payment is rejected due to non-compliance.

Scenario: Process valid SWIFT ISO 20022 payment
  Given the system receives a SWIFT ISO 20022 payment message
  And the payment message includes all mandatory fields (debtor IBAN, creditor IBAN, amount, currency)
  And all fields are valid
  When the payment is processed
  Then the system should process the payment within 10 seconds
  And the system should send the payment to the partner bank

Scenario: Reject payment with missing mandatory field
  Given the system receives a SWIFT ISO 20022 payment message
  And the payment message is missing the debtor IBAN field
  When the payment is processed
  Then the system should reject the payment
  And the system should log the validation failure for audit purposes
  And the system should notify the operations team

Scenario: Reject payment with invalid mandatory field
  Given the system receives a SWIFT ISO 20022 payment message
  And the payment message includes an invalid creditor IBAN field
  When the payment is processed
  Then the system should reject the payment
  And the system should log the validation failure for audit purposes
  And the system should notify the operations team

Scenario: Log all payment transactions for audit
  Given the system processes a SWIFT ISO 20022 payment message
  When the payment is processed
  Then the system should log the transaction details, including validation status, for audit purposes

Scenario: Notify operations team on rejection
  Given the system rejects a SWIFT ISO 20022 payment message due to non-compliance
  When the payment is rejected
  Then the system should notify the operations team about the rejection and the reason for rejection
