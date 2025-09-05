class HashMap:
    def __init__(self,initial_capacity=8,load_factor=0.75):
        if initial_capacity<1:
            initial_capacity=1
        cap=1
        while cap<initial_capacity:
            cap<<=1
        self._buckets=[[] for _ in range(cap)]
        self._size=0
        self._load_factor=load_factor

    def _index(self,key):
        return (hash(key)&0x7FFFFFFF)%len(self._buckets)

    def _resize_if_needed(self):
        if self._size/len(self._buckets)>self._load_factor:
            old_buckets=self._buckets
            new_cap=len(self._buckets)*2
            self._buckets=[[] for _ in range(new_cap)]
            for bucket in old_buckets:
                for k,v in bucket:
                    idx=self._index(k)
                    self._buckets[idx].append((k,v))

    def put(self,key,value):
        idx=self._index(key)
        bucket=self._buckets[idx]
        for i,(k,v) in enumerate(bucket):
            if k==key:
                bucket[i]=(key,value)
                return
        bucket.append((key,value))
        self._size+=1
        self._resize_if_needed()

    def get(self,key):
        idx=self._index(key)
        bucket=self._buckets[idx]
        for k,v in bucket:
            if k==key:
                return v
        return None

    def remove(self,key):
        idx=self._index(key)
        bucket=self._buckets[idx]
        for i,(k,v) in enumerate(bucket):
            if k==key:
                bucket.pop(i)
                self._size-=1
                return True
        return False

    def __len__(self):
        return self._size

    def keys(self):
        res=[]
        for bucket in self._buckets:
            for k,_ in bucket:
                res.append(k)
        return res

    def values(self):
        res=[]
        for bucket in self._buckets:
            for _,v in bucket:
                res.append(v)
        return res

    def items(self):
        res=[]
        for bucket in self._buckets:
            for kv in bucket:
                res.append(kv)
        return res
def main():
    hm=HashMap()
    hm.put("a",1)
    hm.put("b",2)
    hm.put("c",3)
    print(hm.get("b"))
    hm.remove("b")
    print(hm.get("b"))
    print(hm.keys())
    print(hm.values())
    print(hm.items())

if __name__=="__main__":
    main()