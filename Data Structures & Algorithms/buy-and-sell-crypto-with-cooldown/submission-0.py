class Solution:

  def maxProfit(self, prices: list[int]) -> int:
    if not prices:
      return 0

    sold = 0
    held = -prices[0]
    reset = 0

    for price in prices[1:]:
      prev_sold = sold
      sold = held + price
      held = max(held, reset - price)
      reset = max(reset, prev_sold)

    return max(sold, reset)