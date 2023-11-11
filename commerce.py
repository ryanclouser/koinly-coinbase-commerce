#!/usr/bin/env python3
import csv

def main():
	data = []

	with open('commerce.csv') as f:
		reader = csv.reader(f, delimiter=',', quotechar='"')
		for row in reader:
			data.append(row)

	del data[0]

	with open('koinly.csv', 'w') as f:
		writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		writer.writerow(['Date', 'Sent Amount', 'Sent Currency', 'Received Amount', 'Received Currency', 'Fee Amount', 'Fee Currency', 'Label', 'Description', 'TxHash'])

		for i in data:
			date = i[0]
			type = i[2]
			invoice = i[3]
			currency = i[8]
			price = i[9]
			amount = i[10]
			tx = i[-1]

			if type == 'Product Checkout':
				row = [date, '', '', amount[:amount.find(' ')], currency, '', '', 'income', invoice, tx]
				writer.writerow(row)
			elif type == 'Withdrawal':
				row = [date, '-' + amount[:amount.find(' ')], currency, '', '', '', '', '', 'Withdrawal', tx]
				writer.writerow(row)
			else:
				print('Unsupported transaction type %s' % (type))

if __name__ == '__main__':
	main()