# django-crud — 전체 플로우 (한 장)

미리보기에서 **잘리면**: 창을 넓히거나, Zoom 아웃, 또는 [mermaid.live](https://mermaid.live)에 아래 코드만 붙여 넣어 확인하세요.

```mermaid
%%{init: {
  "flowchart": { "useMaxWidth": false, "htmlLabels": true },
  "themeVariables": { "fontSize": "13px" }
}}%%
flowchart LR
    U["브라우저<br/>GET·POST"]

    R["todolist/urls.py<br/>admin · include"]

    T["todos/urls.py<br/>path → 뷰 연결"]

    W["todos/views.py<br/>index · detail · edit · toggle · delete"]

    DB[("SQLite<br/>Todo 모델")]

    FM["todos/forms.py<br/>TodoForm"]

    TP["템플릿<br/>extends base.html"]

    U --> R --> T --> W
    W --> DB
    W --> FM
    W --> TP
    TP -->|HTML| U
```

**읽는 법**

- **왼쪽 → 오른쪽**이 요청이 지나는 순서이고, `템플릿`에서 렌더한 HTML이 다시 **브라우저**로 돌아갑니다.
- `W`에서 아래로 갈라진 **DB / TodoForm / 템플릿**은 뷰가 같은 단계에서 같이 쓰는 자원입니다.

---

### URL → 뷰 (CRUD 보조)

| 경로 | 뷰 | 하는 일 |
|------|-----|---------|
| `""` | `index` | 목록, 새 할 일 추가(Create) |
| `"<pk>/"` | `detail` | 한 건 조회(Read) |
| `"<pk>/edit/"` | `edit_todo` | 제목 수정(Update) |
| `"<pk>/toggle/"` | `toggle_completed` | 완료 여부(Update) |
| `"<pk>/delete/"` | `delete_todo` | 삭제(Delete) |

표는 그림과 겹치지 않게 **보조**만 합니다.
