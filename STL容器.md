## STL容器

array
----

bitset
----

forward_list
----

vector
----
* 序列容器
* 动态内存扩展（每次翻倍）

stack
----

list
----

deque
----

queue
----

map
----
* 用红黑树实现
* 键和值可以不同类型，键值不能重复
* 有序的关联容器
* 查询/插入/删除复杂度：O(logN)

unorder_map
----
* 用哈希算法实现
* 键和值可以不同类型
* 无序的关联容器
* 查询/插入/删除复杂度：O(1)

set
----
* 红黑树实现
* 键和值相同，键值不能重复
* 有序的关联容器
* 查询/插入/删除复杂度：O(logN)

unorder_set
----
* 哈希算法实现
* 键和值相同，不可重复键值，哈希实现目的是为了加快查询速度
* 无序的关联容器
* 查询/插入/删除复杂度：O(1)

备注
----
The more complicated a data structure, the more likely that it's not as widely useful as it might seem.
