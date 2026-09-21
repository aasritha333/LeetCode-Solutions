class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        f=0;s=0
        while s<n:
            if f<=m-1:
                if nums1[f]<=nums2[s]:
                    f+=1
                else:
                    i=m-1
                    while i>=f:
                        nums1[i+1]=nums1[i]
                        i-=1
                    nums1[f]=nums2[s]
                    s+=1;f+=1;m+=1   
            else:
                i=m
                while s<n:
                    nums1[i]=nums2[s]
                    i+=1;s+=1;f+=1;m+=1


            
            

        