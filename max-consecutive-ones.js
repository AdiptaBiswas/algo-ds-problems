"""
* Problem: Max Consecutive Ones
* Problem ref: Leetcode
* Section: Array
"""

var nums = [1,1,0,0,1,1,1,1,0,1,1,1,0,1,1,0,1,1,1,1,1,0,1,0];
var temp, maxi = 0;
for (let i = 0; i < nums.length; i++)
{
  if (nums[i] == 1)
  {
    temp += 1;
  }
  else
  {
    if (temp >= maxi)
    {
      maxi = temp;
    }
    temp = 0;
  }
}
console.log(maxi > temp ? maxi : temp);

""" 
Output: 5
"""
