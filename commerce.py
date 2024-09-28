#!/usr/bin/env python3
import csv

def main():
	data = []

	with open('commerce.csv') as f:
		reader = csv.reader(f, delimiter=',', quotechar='"')
		for row in reader:
			data.append(row)

	# header
	del data[0]

	with open('koinly.csv', 'w') as f:
		writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		writer.writerow(['Date', 'Sent Amount', 'Sent Currency', 'Received Amount', 'Received Currency', 'Fee Amount', 'Fee Currency', 'Label', 'Description', 'TxHash'])

		for i in data:
			completed = i[0]
			date = i[1]
			type = i[2]
			invoice = i[3]

			subtotal = i[10]
			amount = subtotal[:subtotal.find(' ')]
			currency = subtotal[subtotal.find(' ') + 1:]

			cb_fee = i[14]
			if cb_fee:
				cb_fee = cb_fee[:cb_fee.find(' ')]

			net_fee = i[16]
			if net_fee:
				net_fee = net_fee[:net_fee.find(' ')]

			homestead = i[22]

			tx = i[-1]

			if type == 'Product Checkout':
				row = [date, '', '', amount, currency, cb_fee, currency, 'income', invoice, tx]
				writer.writerow(row)

				if homestead:
					row = [completed, '-' + str(float(amount) - float(cb_fee)), currency, '', '', net_fee, currency, '', 'withdrawal', '']
					writer.writerow(row)
			elif type == 'Withdrawal' or type == 'Refund':
				row = [date, '-' + amount, currency, '', '', net_fee, currency, '', 'withdrawal', tx]
				writer.writerow(row)
			else:
				print('Unsupported transaction type %s' % (type))

if __name__ == '__main__':
	main()
