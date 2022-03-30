##!/usr/bin/env python3
## code to attempt Soniya's code exercise at https://leetcode.com/discuss/interview-question/1002811/Amazon-or-OA-20201-or-Fresh-Promotion
import numpy as np

def didyouwin(codeList, shoppingCart):
	if not codeList or not codeList[0]:
		print('codeList empty, customer wins')
		return 1 # customer wins if codeList is empty

	for group in codeList:
		print('Now looking for group', group, 'in', shoppingCart)
		'''
		if group == ['anything']:
			print(shoppingCart[0], 'found in', shoppingCart, 'as "anything"; therefore continuing..\n')
			shoppingCart = shoppingCart[1:]
			print('shoppingCart shortened to', shoppingCart, '\n')

		elif 'anything' in group:
			idx_list = [index for index, val in enumerate(group) if val == 'anything']
			subgroups = [group[i: j] for i, j in zip([0] + (np.array(idx_list) + 1).tolist(), idx_list + ([len(group)] if idx_list[-1] != len(group) else []))]
			print('Deb15: idx_list =', idx_list, 'start stop indices before zip =', [0] + (np.array(idx_list) + 1).tolist(), idx_list + ([len(group)] if idx_list[-1] != len(group) else []), 'subgroups =', subgroups) #
		'''
		#if 'anything' in group:
		for fruit in group:
			idx = np.where(np.array(shoppingCart) == fruit)[0]
			if fruit == 'anything':
				print(shoppingCart[0], 'found in', shoppingCart, 'as "anything"; therefore continuing..\n')
				shoppingCart = shoppingCart[1:]
				print('shoppingCart shortened to', shoppingCart, '\n')
			elif len(idx) > 0:
				print(fruit, 'found in', shoppingCart, 'at', idx[0], '; therefore continuing..\n')
				shoppingCart = shoppingCart[idx[0]+1:]
				print('shoppingCart shortened to', shoppingCart, '\n')
			else:
				print(fruit, 'not found in', shoppingCart, 'customer loses')
				return 0 # fruit not found, customer lost
		'''
		else:
			group_found_at_index = [i for i in range(len(shoppingCart) - len(group) + 1) if group == shoppingCart[i : i + len(group)]]
			if len(group_found_at_index) == 0:
				print(group, 'not found in', shoppingCart, 'customer loses')
				return 0 # group not found anywhere, customer lost
			else:
				print(group, 'found in', shoppingCart, 'at', group_found_at_index, '; therefore continuing..\n')
				shoppingCart = shoppingCart[group_found_at_index[0] + len(group):]
				print('shoppingCart shortened to', shoppingCart, '\n')
		'''
	print('All groups found, customer wins')
	return 1

if __name__ == '__main__':
	codeList = [['orange', 'apple'], ['banana', 'anything', 'banana']]
	shoppingCart = ['orange', 'orange', 'apple', 'banana', 'orange', 'banana']

	result = didyouwin(codeList, shoppingCart)
	print('result =', result)

