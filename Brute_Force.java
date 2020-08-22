// 숫자로 된 배열을 받고 배열의 원소값 두개가 타겟이 될 때
// 그 인덱스 값을 리턴하는 알고리즘
class Solution {
	public int[] twoSum(int[] nums, int target) {
		for (int i = 0; i < nums.length; i++) {
			for (int j = 0; j < nums.length; j++) {
				if (nums[j] == target - nums[i]) {
					return new int[] { i, j };

				}
			}
		}
		throw new IllegalArgumentException("no two num solution!");
	}
}
