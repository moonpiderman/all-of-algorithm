### π§βπ» [ν€ν¨λ λλ₯΄κΈ°](https://programmers.co.kr/learn/courses/30/lessons/67256)

> - μ€λ§νΈν° μ ν ν€ν¨λμ κ° μΉΈμ λ€μκ³Ό κ°μ΄ μ«μλ€μ΄ μ ν μμ΅λλ€.
![initial](https://user-images.githubusercontent.com/70942197/123735424-25962880-d8da-11eb-81c7-fcccf5030c1e.png)
> - μ΄ μ ν ν€ν¨λμμ μΌμκ³Ό μ€λ₯Έμμ μμ§μκ°λ½λ§μ μ΄μ©ν΄μ μ«μλ§μ μλ ₯νλ €κ³  ν©λλ€.
> - λ§¨ μ²μ μΌμ μμ§μκ°λ½μ * ν€ν¨λμ μ€λ₯Έμ μμ§μκ°λ½μ # ν€ν¨λ μμΉμμ μμνλ©°, μμ§μκ°λ½μ μ¬μ©νλ κ·μΉμ λ€μκ³Ό κ°μ΅λλ€.
> > 1. μμ§μκ°λ½μ μνμ’μ° 4κ°μ§ λ°©ν₯μΌλ‘λ§ μ΄λν  μ μμΌλ©° ν€ν¨λ μ΄λ ν μΉΈμ κ±°λ¦¬λ‘ 1μ ν΄λΉν©λλ€.
> > 2. μΌμͺ½ μ΄μ 3κ°μ μ«μ 1, 4, 7μ μλ ₯ν  λλ μΌμ μμ§μκ°λ½μ μ¬μ©ν©λλ€.
> > 3. μ€λ₯Έμͺ½ μ΄μ 3κ°μ μ«μ 3, 6, 9λ₯Ό μλ ₯ν  λλ μ€λ₯Έμ μμ§μκ°λ½μ μ¬μ©ν©λλ€.
> > 4. κ°μ΄λ° μ΄μ 4κ°μ μ«μ 2, 5, 8, 0μ μλ ₯ν  λλ λ μμ§μκ°λ½μ νμ¬ ν€ν¨λμ μμΉμμ λ κ°κΉμ΄ μμ§μκ°λ½μ μ¬μ©ν©λλ€.
> > 5. λ§μ½ λ μμ§μκ°λ½μ κ±°λ¦¬κ° κ°λ€λ©΄, μ€λ₯Έμμ‘μ΄λ μ€λ₯Έμ μμ§μκ°λ½, μΌμμ‘μ΄λ μΌμ μμ§μκ°λ½μ μ¬μ©ν©λλ€.
> - μμλλ‘ λλ₯Ό λ²νΈκ° λ΄κΈ΄ λ°°μ΄ numbers, μΌμμ‘μ΄μΈμ§ μ€λ₯Έμμ‘μ΄μΈ μ§λ₯Ό λνλ΄λ λ¬Έμμ΄ handκ° λ§€κ°λ³μλ‘ μ£Όμ΄μ§ λ, κ° λ²νΈλ₯Ό λλ₯Έ μμ§μκ°λ½μ΄ μΌμμΈ μ§ μ€λ₯ΈμμΈ μ§λ₯Ό λνλ΄λ μ°μλ λ¬Έμμ΄ ννλ‘ return νλλ‘ solution ν¨μλ₯Ό μμ±ν΄μ£ΌμΈμ.

> μ ν μ¬ν­
> 
> - numbers λ°°μ΄μ ν¬κΈ°λ 1 μ΄μ 1,000 μ΄νμλλ€.
> - numbers λ°°μ΄ μμμ κ°μ 0 μ΄μ 9 μ΄νμΈ μ μμλλ€.
> - handλ "left" λλ "right" μλλ€.
> - μΌμ μμ§μκ°λ½μ μ¬μ©ν κ²½μ°λ L, μ€λ₯Έμ μμ§μκ°λ½μ μ¬μ©ν κ²½μ°λ Rμ μμλλ‘ μ΄μ΄λΆμ¬ λ¬Έμμ΄ ννλ‘ return ν΄μ£ΌμΈμ.

> μμΆλ ₯ μ
> 
> |numbers|hand|result|
> |:---|:---|:---|
> |[1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]|"right"|"LRLLLRLLRRL"|
> |[7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]|"left"|"LRLLRRLLLRR"|
> |[1, 2, 3, 4, 5, 6, 7, 8, 9, 0]|"right"|"LLRLLRLLRL"|
