### π§βπ» λ¬Έμ  No. 42577

> μ νλ²νΈλΆμ μ ν μ νλ²νΈ μ€, ν λ²νΈκ° λ€λ₯Έ λ²νΈμ μ λμ΄μΈ κ²½μ°κ° μλμ§ νμΈνλ € ν©λλ€.
> μ νλ²νΈκ° λ€μκ³Ό κ°μ κ²½μ°, κ΅¬μ‘°λ μ νλ²νΈλ μμμ΄μ μ νλ²νΈμ μ λμ¬μλλ€.
>
> - κ΅¬μ‘°λ 119
> - λ°μ€μ : 97 674 223
> - μ§μμ : 11 9552 4421
>   μ νλ²νΈλΆμ μ ν μ νλ²νΈλ₯Ό λ΄μ λ°°μ΄ phone_book μ΄ solution ν¨μμ λ§€κ°λ³μλ‘ μ£Όμ΄μ§ λ, μ΄λ€ λ²νΈκ° λ€λ₯Έ λ²νΈμ μ λμ΄μΈ κ²½μ°κ° μμΌλ©΄ falseλ₯Ό κ·Έλ μ§ μμΌλ©΄ trueλ₯Ό return νλλ‘ solution ν¨μλ₯Ό μμ±ν΄μ£ΌμΈμ.

> μ ν μ¬ν­
>
> - phone_bookμ κΈΈμ΄λ 1 μ΄μ 1,000,000 μ΄νμλλ€.
> - κ° μ νλ²νΈμ κΈΈμ΄λ 1 μ΄μ 20 μ΄νμλλ€.
> - κ°μ μ νλ²νΈκ° μ€λ³΅ν΄μ λ€μ΄μμ§ μμ΅λλ€.

> μμΆλ ₯ μμ
> 
> | phone_book                         | return |
> | :--------------------------------- | :----- |
> | ["119", "97674223", "1195524421"]  | false  |
> | ["123", "456", "789"]              | true   |
> | ["12", "123", "1235", "567", "88"] | false  |

> μμΆλ ₯ μ μ€λͺ
>
> - ν λ²νΈκ° λ€λ₯Έ λ²νΈμ μ λμ¬μΈ κ²½μ°κ° μμΌλ―λ‘, λ΅μ trueμλλ€.
> - μ²« λ²μ§Έ μ νλ²νΈ, β12βκ° λ λ²μ§Έ μ νλ²νΈ β123βμ μ λμ¬μλλ€. λ°λΌμ λ΅μ falseμλλ€.

### π§βπ» Solution

1. μ²«μ§Έλ‘ startswith ν¨μμ λν μ΄ν΄κ° νμνλ€.
2. startswith ν¨μλ No list, No dict, Only Tuple
3. sortλ₯Ό μ¬μ©ν μ΄μ λ λ¬Έμμ΄μ λμ΄ν΄μ£Όλ κ²μ΄ νμνκΈ° λλ¬Έμ΄λ€.
4. κ·ΈλμΌ νμμ΄ λ³΄λ€ μμν΄μ§λ€.
