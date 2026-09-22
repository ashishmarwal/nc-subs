class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> keyedAnagrams = new HashMap<>();

        for(String str : strs) {
            int[] counts = new int[26];

            for (int i = 0; i < str.length(); i++) {
                char ch = str.charAt(i);
                int idx = ch - 'a';
                counts[idx] = counts[idx] += 1;
            }

            // convert counts to a key
            String key = Arrays.toString(counts);
            keyedAnagrams.putIfAbsent(key, new ArrayList<>());
            keyedAnagrams.get(key).add(str);
        }

        return new ArrayList<>(keyedAnagrams.values());
    }
}
