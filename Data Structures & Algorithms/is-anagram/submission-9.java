class Solution {
    public boolean isAnagram(String s, String t) {
        if (s == null || t == null || s.length() != t.length()) {
            return false;
        }

        // freq map
        Map<Character, Integer> freqsA = new HashMap<>();
        Map<Character, Integer> freqsB = new HashMap<>();

        for (int i = 0; i < s.length(); i++) {
            freqsA.put(s.charAt(i), freqsA.getOrDefault(s.charAt(i), 0) + 1);
            freqsB.put(t.charAt(i), freqsB.getOrDefault(t.charAt(i), 0) + 1);
        }

        System.out.println("Map1" + freqsA);
        System.out.println("Map2" + freqsB);

        if (freqsA.size() != freqsB.size()) {
            return false;
        }

        Iterator<Character> it = freqsA.keySet().iterator();
        while(it.hasNext()) {
            Character c = it.next();
            System.out.println("C :: " + c);

            int charFreqA = freqsA.get(c);
            Integer charFreqB = freqsB.get(c);

            if (charFreqB == null) {
                return false;
            }

            System.out.println(c + " -> freqsA.get(c) = " + charFreqA + " freqsB.get(c) = " + charFreqB);

            if (charFreqA != charFreqB) {
                System.out.println("DAMN!");
                return false;
            }
        }

        return true;
    }
}
