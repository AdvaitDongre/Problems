class hi {
    public int[] nextGreaterElement(int[] nums1, int[] nums2) {
        int result[nums2.size()];
        for (int i=0;i<nums1.size();i++){
            for (int j=0;j<nums2.size();j++){
                if (nums1[i] == nums2[j]){
                    if (nums2[j]<nums2[j+1]){
                        result.add(-1);
                    }
                    else{
                        result.add(nums2[j+1]);
                    }
                }
            }
        }
        return result;
    }
}