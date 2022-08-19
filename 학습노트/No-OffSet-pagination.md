# No-Offset-Pagination

- 1억건이 넘는 테이블에서의 페이징은 단순 인덱스만 태운다고해서 성능 문제가 해결되지는 않는다.
- 기존의 페이징 방식이 `페이지 번호` `페이지 사이즈` 를 기반으로 한다면 No Offset은 페이지 번호가 없는 더보기 (More) 방식을 이야기 한다.

기존에 사용 하는 페이징 쿼리는 일반적으로 다음과 같다.

```sql
SELECT *
FROM items
ORDER BY id DESC
OFFSET 페이지번호
LIMIT 페이지사이즈
```

이와 같은 형태의 페이징 쿼리가 뒤로갈수록 느린 이유는 결국 앞에서 읽었던 행을 다시 읽어야 하기 때문이다.

예를 들어 offset 10000, limit 20 이라고 한다면 최종적으로 10,020개의 행을 읽어야 한다.

No Offset 방식은 조회 시작 부분을 인덱스로 빠르게 찾아 매번 첫 페이지만 읽도록 하는 방식이다.

```sql
SELECT *
FROM items
WHERE 조건문
AND id < 마지막조회ID # 직전 조회 결과의 마지막 id
ORDER BY id DESC
LIMIT 페이지사이즈
```

실제로 limit 과 next_id를 적용하여 필수로 페이지네이션을 구현해야한다.

기본 제한 갯수는 50으로 설정한다.
