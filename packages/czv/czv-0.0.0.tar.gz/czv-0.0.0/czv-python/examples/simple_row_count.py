import czv

data: str = """fruits,price
apple,2.50
banana,3.00
strawberry,1.50"""

output: int = czv.row_count(file_data=data, include_header_row=True)

print(output) # 4
