class Solution {
    public boolean isAnagram(String s, String t) {
        if (s == null || t == null || s.length() != t.length()) {
            return false;
        }

        String sortedS = sortString(s);
        String sortedT = sortString(t);

        for (int i = 0; i < s.length(); i++) {
            if (sortedS.charAt(i) != sortedT.charAt(i)) {
                return false;
            }
        }

        return true;
    }

    private String sortString(String input) {
        char[] strArr = input.toCharArray();
        Arrays.sort(strArr);
        return new String(strArr);
    }
}
