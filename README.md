# python-produce-consumer


## Getting Started

**Goal** π: λ©ν° νλ‘μΈμ€ νΉμ λ©ν° μ€λ λλ₯Ό λ°©μμΌλ‘ μμ°μ/μλΉμ ν¨ν΄μ κ΅¬ννκ³  μ±λ₯μ μμΈ‘νλ€.

**Metrics** 
- μ΄λΉ μ§νν  μ μλ μμμ μ
- μ΅μ μ μλΉμ μ

## Method
- Multiprocessing : CPU bound

νμ΄μ¬μλ GILμ΄λΌλ λ½μ΄ μ‘΄μ¬νκ³  μ΄λ μΈν°νλ¦°ν°κ° νλ²μ νλμ μ€λ λλ§ λμνλλ‘ νλ€.
κ·Έλ¬λ―λ‘ CPU bound μμμμλ λ©ν°μ€λ λλ₯Ό μ¬μ©ν  κ²½μ° μ±λ₯μ μΈ μ΄μκ° λ°μνλ€.

- Multithreading or AsyncIO: I/O bounding 

I/O Bound μμμΈ κ²½μ° Lockλ³΄λ€λ λ λΉ λ₯Ό μ μλ€.

### Creating Virtual Evironment
κ°μνκ²½ μμ±
```
PIPENV_VENV_IN_PROJECT=true pipenv install --three
```

## Reference
- [multiprocessing](https://docs.python.org/ko/3/library/multiprocessing.html)


## License
- MIT
