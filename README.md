# Korean_Catholic
It is a Korean Catholic LLM project

# Korean Catholic RAG System (가톨릭 문서 기반 RAG 시스템)

## 📌 개요

이 프로젝트는 Korean Catholic 문서를 대상으로 한 NLP 기반의 RAG(Retrieval-Augmented Generation) 시스템입니다. SentenceTransformer와 Huggingface 기반의 LLM을 통해 사용자의 질문에 적절한 답변을 생성합니다.

향후에는 강론 작성, 교리 교육 도우미 등의 기능으로 확장하는 것을 목표로 하고 있습니다.

---

## 📁 프로젝트 구조

```
├── ChromaRAGSystem.py       # RAG 파이프라인 클래스
├── setting.py               # DB 로드 및 모델 세팅
├── task030.py               # CLI 기반 실행 스크립트
├── korean_catholic_data/    # 현재 보유 중인 벡터 DB
├── README.md                # 현재 문서
```

---

## 🚀 실행 방법

1. `./korean_catholic_data` 경로에 ChromaDB 데이터베이스가 존재하는지 확인
2. `setting.py` 내 모델 캐시 경로를 환경에 맞게 수정
3. CLI 실행:

```bash
python task030.py
```

종료 시 `'quit'` 또는 `'종료'` 입력

---

## 🔍 파일 설명

### `ChromaRAGSystem.py`
- `retrieve_relevant_docs(query)`: 입력 질문에 대한 유사 문서 검색
- `generate_response(query, context_docs)`: 검색된 문서를 context로 활용하여 답변 생성
- `query(question)`: 전체 RAG 파이프라인 실행

### `setting.py`
- `load_chroma_db(path)`: 로컬에 저장된 ChromaDB 로드
- `build_RAG_system(path)`: 임베딩 모델, LLM, 파이프라인 초기화

### `task030.py`
- CLI 기반 인터페이스 제공
- 사용자 질문 입력 → 실시간 답변 출력

---

## 🧠 모델 정보

| 항목          | 모델명                                         |
|---------------|------------------------------------------------|
| 임베딩 모델   | `all-MiniLM-L6-v2` (SentenceTransformer)       |
| LLM           | `Bllossom/llama-3.2-Korean-Bllossom-3B`        |
| 생성 파이프라인 | Huggingface `pipeline(text-generation)`      |

---

## 🛠 개발 환경

- CPU: AMD Ryzen 7 6800H
- GPU: NVIDIA RTX 3060
- RAM: 32GB
- Os : Window 11

---

## 📚 문헌 출처

- 『알고싶은 가톨릭 신학 1』 - 제1장: 그리스도교

---

## 📝 라이선스

---

## 🙋‍♂️ 작성자

- 김원재
- Email: dodug2e@gmail.com
