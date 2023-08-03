import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Date;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Scanner;
import java.util.Set;
import java.util.SortedSet;
import java.util.TreeSet;
import java.util.stream.Collectors;

class Solution {
    public boolean containsNearbyAlmostDuplicate(int[] nums, int indexDiff, int valueDiff) {
        if (indexDiff < 1 || valueDiff < 0)
            return false;

        String s = "";
        char c = 0;
        s.contains(new String(new char[]{c}));
        
        SortedSet<Integer> set = new TreeSet<>();
        for (int i = 0; i < nums.length; i++) { 
            int leftBoundary = nums[i] - valueDiff;
            int rightBoundary = nums[i] + valueDiff + 1;

            Set<Integer> subset = set.subSet(leftBoundary, rightBoundary);

            if (subset.size() != 0)
                return true;
            
            set.add(nums[i]);
            
            if (i >= indexDiff)
                set.remove(nums[i-indexDiff]);
        }

        return false;
    }

    public static void main(String[] args) {
    //   Solution solution = new Solution();

    //   Scanner scanner = new Scanner(System.in);
    //   String numsStr = scanner.next();

    //   numsStr = numsStr.replace("[", "");
    //   numsStr = numsStr.replace("]", "");

    //   int[] nums = Arrays.stream(numsStr.split(",")).mapToInt(Integer::parseInt).toArray();

    //   int indexDiff = scanner.nextInt();
    //   int valueDiff = scanner.nextInt();

    //   scanner.close();

    //   Date date = new Date();

    //   boolean isComplete = solution.containsNearbyAlmostDuplicate(nums, indexDiff, valueDiff);

    //   Date dateNow = new Date();

    //   SimpleDateFormat sf = new SimpleDateFormat("s");

    //   long timeDiff = dateNow.getTime() - date.getTime();
    //   System.out.println("Time of execution: " + sf.format(timeDiff));

    //   System.out.println("The value resolved to: " + isComplete);

        /**
         * Anagram
         */
        // String s = "anagram";
        // String t = "nagaram";
    
        // List<String> valS = Arrays.asList(s.split(""));
        // Collections.sort(valS);
        // String sortedS = valS.stream().collect(Collectors.joining());

        // List<String> valT = Arrays.asList(t.split(""));
        // Collections.sort(valT);
        // String sortedT = valS.stream().collect(Collectors.joining());

        // if (sortedS.equals(sortedT))
        //     System.out.println(true);
        // else
        //     System.out.println(false);

        /**
         * Two sum
         */
        // int[] twoSumIndices = twoSum(new int[]{2,7,11,15}, 9);
        // for (int i : twoSumIndices) {
        //     System.out.print(i);
        // }

        /**
         * Top k frequents
         */
        // int[] itemList = topKFrequent(new int[]{1,1,1,2,2,3}, 2);
        // Arrays.stream(itemList).forEach(val -> System.out.println(val));

        // Arrays.stream(productExceptSelf(new int[]{-1,1,0,-3,3})).forEach(val -> System.out.println(val));

        System.out.println(maxProduct(new int[]{2,3,-2,4/*,-4,-3*//*,3,-1,4*/}));
    }

    public static int maxProduct(int[] nums) {
        // create an array with result use list

        if (nums.length == 1) {
            return nums[0];
        }

        int tempProd = nums[0];
        for (int i = 0; i < nums.length; i++) {
            int product = 0;
            int numElems = 1;

            for (int j = i+1; j < numElems + (i + 1); j++) {
                if (j != nums.length-1) {
                    numElems++;
                } else break;

                if (tempProd < nums[j])
                    tempProd = nums[j];

                product *= nums[j];
                if (tempProd < product)
                    tempProd = product;
            }
        }

        return tempProd;
    }

    public static int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            if (map.containsKey(target-nums[i]))
                return new int[]{map.get(target-nums[i]), i};
            map.put(nums[i], i);
        }

        return new int[]{};
    }

    public static int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> mostFrequent = new HashMap<>();

        for (int elm : nums) {
            if (mostFrequent.containsKey(elm)) {
                mostFrequent.put(elm, mostFrequent.get(elm) + 1);
            } else {
                mostFrequent.put(elm, 1);
            }
        }

        List<Map.Entry<Integer, Integer>> entryList = new ArrayList<>(mostFrequent.entrySet());
        entryList.sort(Map.Entry.<Integer, Integer>comparingByValue().reversed());

        int[] frequents = new int[k];
        for (int i = 0; i < entryList.size() && i < k; i++) {
            frequents[i] = entryList.get(i).getKey();
        }

        return frequents;
    }

    public static int[] productExceptSelf(int[] nums) {
        int[] productArr = new int[nums.length];

        int product = 0;
        boolean hasZero = false;
        for (int i = 0; i < nums.length; i++) {
            if (i == 0 && product == 0) {
                product = nums[i];
                continue;
            } else if (i > 0 && product == 0) {
                hasZero = true;
                product = nums[i];
                continue;
            }

            int prodTemp = product;
            product *= nums[i];
            
            // if (product == 0) {
            //     hasZero = true;
            //     product = prodTemp;
            // }
        }

        for (int i = 0; i < nums.length; i++) {
            if (hasZero && nums[i] != 0) {
                productArr[i] = 0;
                continue;
            }

            if (nums[i] == 0) {
                productArr[i] = product;
                continue;
            }
            
            if (!hasZero) {
                productArr[i] = product/nums[i];
            }
        }

        return productArr;
    }
}