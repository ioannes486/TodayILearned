# [spring] spring jdbc에서 select쿼리를 실행하는 메서드를 실행시키기 위해서 해당 모델에 setter메서드가 필요한 이유

날짜: 2025년 8월 24일
진행상황: 시작 전

# Spring JDBC에서 Setter가 필요한 이유

`JdbcTemplate` 으로 조회할 때

`javaspringJdbcTemplate.queryForObject(
        SELECT_QUERY,
        new BeanPropertyRowMapper<>(Course.class),
        id);`

처럼 **`BeanPropertyRowMapper`**를 쓰면, 이 매퍼가 ResultSet → 자바 객체(Course)를 만드는 과정을 자동화합니다.

동작 원리는 다음과 같습니다.

1. **컬럼 이름 → 자바 프로퍼티 이름 매핑**
    - DB 컬럼을 스네이크→카멜 케이스로 변환(`author_name` → `authorName`)
    - 매핑 규칙에 따라 `Course` 클래스에 동일한 프로퍼티가 있는지 확인
2. **리플렉션으로 Setter 호출**
    - 프로퍼티가 있으면 `setAuthorName(String value)` 같은 **setter 메서드**를 찾습니다.
    - Setter가 존재하면 리플렉션으로 호출하여 값 주입
3. **필드 주입은 시도하지 않음**
    - 기본 설정(default)에서는 필드에 직접 접근하지 않고 **public setter만 사용**합니다.
    - 따라서 setter가 없으면 해당 프로퍼티는 값이 채워지지 않고 `null`/`0`으로 남습니다.
    - 모든 필드의 setter가 없으면 매핑된 객체는 비어 있게 되어 “쿼리가 안 되는 것처럼” 보입니다.

## 왜 setter 없이 필드에 직접 주입하지 않을까?

BeanPropertyRowMapper는 스프링 초창기 자바빈(JavaBean) 규격을 따른 구현입니다.

- JavaBean 규격 – “프로퍼티는 `getXxx()/setXxx()` 메서드로 노출한다.”
    
    (Eclipse/IDE 대부분의 코드 생성, 스프링의 BeanUtils 등도 같은 규칙을 따름)
    
- 결과적으로 “setter = 프로퍼티 존재”라는 가정으로 구현돼 있습니다.

## 해결 방법 3가지

| 방법 | 코드 예시 | 특징 |
| --- | --- | --- |
| 1. **Setter 추가** | `java public void setAuthor(String author){ this.author = author; }` |  |
| 2. **Lombok @Setter** | `java @Setter public class Course { ... }` |  |
| 3. **BeanPropertyRowMapper 옵션 변경** | `java var mapper = BeanPropertyRowMapper.newInstance(Course.class, false);` |  |

*세 번째 방법*은 **Spring 5.3 이상**에서 `BeanPropertyRowMapper.newInstance(TargetClass, /* allowRowMapperNull = */ false)` 시그니처로 필드 주입을 켤 수 있습니다. 더 구버전이라면 `mapper.setPrimitivesDefaultedForNullValue(false); mapper.setConversionService(...)` 등 수동 설정이 필요합니다.

## 요약

BeanPropertyRowMapper는 기본적으로 **JavaBean 프로퍼티 규칙**에 따라 **setter를 통해서만** 값을 주입합니다. 따라서 setter가 없는 도메인 클래스는 조회 시 값이 설정되지 않아 “쿼리 결과가 없는” 것처럼 보입니다.

Setter를 추가하거나, Lombok을 쓰거나, 매퍼를 필드 접근 모드로 설정하면 문제를 해결할 수 있습니다.

select 쿼리를 시도할 때는 BeanPropertyRowMapper를 사용하는데 이것은 db의 언어인 스네이크 케이스를 케멀 케이스로 자동으로 바꿔서 매핑해준다.

이 매퍼가 처음 설계될 때 setter를 통해서만 Course의 멤버를 바꾸도록 선언되었기 때문에 select를 실행하는 메서드를 실행시키기 위해서는 해당 클래스에 setter메서드가 필요하다