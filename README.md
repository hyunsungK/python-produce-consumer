# python-produce-consumer


## Getting Started

**Goal** 🚀: 멀티 프로세스 혹은 멀티 스레드를 방식으로 생산자/소비자 패턴을 구현하고 성능을 예측한다.

**Metrics** 
- 초당 진행할 수 있는 작업의 수
- 최적읜 소비자 수

## Method
- Multiprocessing : CPU bound
파이썬에는 GIL이라는 락이 존재하고 이는 인터프린터가 한번에 하나의 스레드만 동작하도록 한다.
그러므로 CPU bound 작업에서는 멀티스레드를 사용할 경우 성능적인 이슈가 발생한다.

- Multithreading or AsyncIO: I/O bounding 
I/O Bound 작업인 경우 Lock보다는 더 빠를 수 있다.

### Creating Virtual Evironment
가상환경 생성
```
PIPENV_VENV_IN_PROJECT=true pipenv install --three
```

## Reference
- [multiprocessing](https://docs.python.org/ko/3/library/multiprocessing.html)


## License
- MIT
