Grid Ref Num scrapper/API

To start the server:
`uvicorn server:app --reload`

How to use the scrapper:
`./uk_grid_ref.py W22HR N90NR NW14NR A7A7A`

output:
```
1 Postcode: W22HR
Grid Reference: TQ 27282 81421
----------------------------------
2 Postcode: N90NR
Grid Reference: TQ 34275 93320
----------------------------------
3 Postcode: NW14NR
Grid Reference: TQ 28378 82666
----------------------------------
4 Postcode: A7A7A
Grid Reference: No data found for this postcode
```