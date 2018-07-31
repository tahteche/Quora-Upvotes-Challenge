import unittest, upvotes

class TestUpvotes(unittest.TestCase):
	def test_get_non_incr_subranges(self):
		items = [1, 2, 1, 4, 5, 7, 7, 8, 9, 0]
		expected = [
			[[1, 2]],
			[[1, 2]],
			[],
			[],
			[[5, 6]],
			[[5, 6]],
			[],
			[[8, 9]]
		]
		n = 10
		k = 3
		output = []
		for start in xrange(0, n-k+1):
			stop = start + k
			output = upvotes.get_non_incr_subranges(start, stop, items,
				output)
			self.assertEqual(output, expected[start])

	def test_get_non_decr_subranges(self):
		items = [1, 2, 1, 4, 5, 7, 7, 8, 9, 0]
		expected = [
			[[0, 1]],
			[[2, 3]],
			[[2, 4]],
			[[3, 5]],
			[[4, 6]],
			[[5, 7]],
			[[6, 8]],
			[[7, 8]]
		]
		n = 10
		k = 3
		output = []
		for start in xrange(0, n-k+1):
			stop = start + k
			output = upvotes.get_non_decr_subranges(start, stop, items,
				output)
			self.assertEqual(output, expected[start])

	def test_sum_subranges(self):
		subranges = [[0, 2], [6, 10]]
		previous_sum =2

		# Sum of the subranges in {subranges} is 13. Adding the 
		# previous_sum should give an expected total of 15
		expected = 15

		sum_of_subs = upvotes.sum_subranges(subranges, previous_sum)
		self.assertEqual(sum_of_subs, expected)