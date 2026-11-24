# Design & App Dev Hub

**웹 디자인 · 프론트엔드 · 네이티브 Android · React Native · Flutter**에 사용하는 GitHub 도구 **225개 / 18개 분야**입니다.

[로보틱스 모음으로](README.md) · [검색·필터 HTML](design-app-dev.html) · [전체 JSON](design-app-dev.catalog.json)

HTML은 파일을 내려받아 브라우저에서 열면 검색·분야·플랫폼·종류·추천·최근 push 정렬을 사용할 수 있습니다. GitHub의 파일 화면은 HTML 소스만 표시하며, 실행 페이지 배포와는 다릅니다.

## 반드시 포함: Taste Skill

**[Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill)** — 사용자가 직접 지정한 필수 항목입니다.

레퍼런스 이미지, 타이포그래피, 팔레트, 레이아웃, 인터랙션과 브라우저 검사를 다루는 **AI 코딩 에이전트용 웹 디자인 스킬**입니다. Android Compose 컴포넌트나 APK 빌더와는 역할이 다릅니다.

현재 README에 명시된 설치 예시입니다. 이 정리 작업에서 스킬이나 외부 설치 스크립트를 실행하지 않았습니다.

```bash
npx skills add https://github.com/Leonxlnx/taste-skill --skill "design-taste-frontend"
```

Node·브라우저 등 요구사항과 설치 명령은 원본 README를 다시 확인하세요.

## 분야별 바로가기

| 분야 | 키 | 개수 |
|---|---|---:|
| [AI 디자인 · 에이전트 스킬](#sector-ai-design) | `ai-design` | 24 |
| [React · 웹 UI 컴포넌트](#sector-react-ui) | `react-ui` | 17 |
| [Vue · Svelte · 기타 웹 UI](#sector-vue-svelte) | `vue-svelte` | 11 |
| [CSS · 스타일 · 디자인 토큰](#sector-css) | `css` | 8 |
| [애니메이션 · 스크롤 · 3D](#sector-motion) | `motion` | 11 |
| [아이콘 · 폰트 · 일러스트](#sector-assets) | `assets` | 10 |
| [프로토타입 · 디자인 · 문서화](#sector-design-tools) | `design-tools` | 8 |
| [차트 · 데이터 화면 · 대시보드](#sector-charts) | `charts` | 11 |
| [웹 프레임워크 · 앱 기반](#sector-web-framework) | `web-framework` | 10 |
| [Android 공식 샘플 · 앱 구조](#sector-android-samples) | `android-samples` | 12 |
| [Jetpack Compose UI · 인터랙션](#sector-compose) | `compose` | 13 |
| [Android 데이터 · 네트워크 · 아키텍처](#sector-android-core) | `android-core` | 15 |
| [Android 카메라 · BLE · 미디어 · 장치](#sector-android-device) | `android-device` | 12 |
| [React Native · Flutter · 크로스플랫폼](#sector-cross-platform) | `cross-platform` | 10 |
| [모바일 UI · 탐색 · 모션](#sector-mobile-ui) | `mobile-ui` | 13 |
| [테스트 · 접근성 · 품질 검사](#sector-testing) | `testing` | 13 |
| [개발 도구 · 빌드 · API · 릴리스](#sector-developer) | `developer` | 18 |
| [참고 자료 · 패턴 · 모음집](#sector-reference) | `reference` | 9 |

## 프로젝트별 시작 조합

| 만들려는 것 | 먼저 볼 조합 | 실제 실행에 필요한 것 |
|---|---|---|
| 웹 랜딩·포트폴리오 | Taste Skill + Vite/Astro + Tailwind + Lucide | 웹 빌드·브라우저 검증 |
| 웹 대시보드 | shadcn/ui 또는 Mantine + ECharts/uPlot + TanStack Table | 데이터 API·웹 테스트 |
| 네이티브 Android | Android Skills + Now in Android + Compose Samples + Coil | Android SDK·JDK·Gradle·서명·실기기 |
| 빠른 크로스플랫폼 앱 | Expo + React Native Paper + React Navigation | 개발 빌드/APK·권한·실기기 검증 |
| Flutter 앱 | Flutter + Riverpod 또는 BLoC + FL Chart | Flutter SDK·Android 툴체인·APK 검증 |
| EMG·BLE 보조장치 앱 | Compose + Nordic BLE + Vico + 로컬 DB + FastAPI(서버가 필요할 때) | BLE 권한·기기 프로토콜·연결 끊김 처리 |
| 카메라·QR 앱 | CameraX 샘플 또는 VisionCamera + QR 라이브러리 | 카메라 권한·저장소 정책·폰/태블릿 테스트 |

대안 라이브러리는 한꺼번에 설치하지 않고 플랫폼·역할별로 선택합니다. 웹 전용 UI를 네이티브 Android UI로 바로 가져올 수는 없습니다. 웹 앱·PWA와 설치 가능한 APK/AAB를 구분합니다.

## 소스 선택 다운로드

로보틱스 카탈로그와 별도 도구를 제공합니다. 소스를 받을 뿐 의존성·모델 설치·앱 빌드·장치 제어는 하지 않습니다.

```bash
python design_hub.py sectors
python design_hub.py list --category ai-design
python design_hub.py list --category android-samples
python design_hub.py fetch --repo Leonxlnx/taste-skill --dry-run
python design_hub.py fetch --category compose
python design_hub.py fetch --category mobile-ui
```

기본 경로는 `design-tools/<owner>--<repo>/`입니다. 추천만 받으려면 `--recommended`, 전체 활성 항목은 `--all`을 사용합니다. 보관된 저장소는 기본 선택에서 제외하며 `--include-archived`로 포함할 수 있습니다. 기존 다운로드·수정 내용은 덮어쓰지 않습니다.

## 확인 범위

- 확인일: **2026-11-24**. 총 225개 중 **220개는 README 앞부분과 메타데이터**, 나머지는 저장소 설명·메타데이터로 확인했습니다.
- **활성 저장소 218개 / 보관됨 7개 / 추천 51개**. 보관된 항목은 과거 예제·기존 앱 유지보수 참고용입니다.
- 생성일과 최근 push 시각은 UTC입니다. push는 릴리스일·기본 브랜치 마지막 기능 변경일과 다릅니다.
- 아래 설명은 용도 정리이며, 설치·빌드·Android 폰/태블릿 호환성·성능을 실행 검증한 결과는 아닙니다.
- 코드가 공개되어 있어도 라이선스가 모두 같지는 않습니다. 서비스·유료 컴포넌트·폰트·브랜드·에셋 조건은 별도입니다. `NOASSERTION`/미표시는 자유 사용 허가가 아닙니다.
- 프롬프트·스킬·UI 라이브러리·샘플·SDK·모음집을 종류별로 표시했습니다. 모음집의 자식 링크는 이 숫자에 중복 집계하지 않습니다.
- 원본 코드는 복제해 합치지 않았습니다. 각 항목의 README·API 메타데이터·조회 시각은 JSON에 기록했습니다.

## 전체 목록

★ 검토 우선 추천 · **필수** 사용자 지정 · **보관됨** archived

<a id="sector-ai-design"></a>

### AI 디자인 · 에이전트 스킬 · 24개

에이전트에 디자인 판단·검토 흐름을 제공하는 지침입니다. UI 라이브러리나 Android 런타임과는 구분합니다.

| 프로젝트 | 플랫폼 · 종류 | 무엇에 쓰나 | 적용 메모 |
|---|---|---|---|
| [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) **필수** ★ | Web · Skill | 사용자 지정 필수: 레퍼런스·타이포·레이아웃·브라우저 검사 기반 웹 디자인 | 필수 포함; Android Compose UI 라이브러리는 아님 |
| [android/skills](https://github.com/android/skills) ★ | Android · Skill | Google 공식 Android 개발·Compose·성능·테스트 지침 | Android 공식 가이드 기반 |
| [anthropics/skills](https://github.com/anthropics/skills) ★ | Web · Skill | frontend-design·문서·브라우저 테스트 등 에이전트 스킬 | frontend-design 경로부터; 라이선스는 스킬별 확인 |
| [emilkowalski/skills](https://github.com/emilkowalski/skills) ★ | Web · Skill | 디자인 엔지니어링·인터랙션·UI 품질 지침 | 타이포·모션·터치 디테일 참고 |
| [expo/skills](https://github.com/expo/skills) ★ | React Native, Android · Skill | Expo 개발·배포·업그레이드·디버깅 공식 스킬 | Expo 프로젝트에 적합 |
| [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) ★ | Web, Mobile · Skill | 스타일·팔레트·폰트·UX·스택별 디자인 지침 | 지원 스택·설치 방법은 원본 확인 |
| [pbakaus/impeccable](https://github.com/pbakaus/impeccable) ★ | Web · Skill | UI 디자인 비평·감사·개선 워크플로 | 기존 화면을 다듬는 용도 |
| [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) ★ | Web, React Native · Skill | React·웹 인터페이스·React Native 개발 지침 | 각 스킬의 적용 조건 확인 |
| [alexiseverage/aesthetic-frontend-skills](https://github.com/alexiseverage/aesthetic-frontend-skills) | Web · Skill | 프론트엔드 미학·타이포·토큰 실험 스킬 | 실험적 프로젝트 |
| [bergside/design-md-chrome](https://github.com/bergside/design-md-chrome) | Web · Tool | 웹사이트 스타일을 DESIGN.md·디자인 스킬로 추출 | 분석 대상 사이트의 사용 권한 확인 |
| [boburxd/broom-design](https://github.com/boburxd/broom-design) | Web · Skill | 디자인 검사·시스템 생성·UI 품질 지침 | 여러 디자인 규칙을 무조건 중첩하지 않기 |
| [charliesbot/android-design](https://github.com/charliesbot/android-design) | Android · Skill | Material 3 Expressive·Compose 화면 디자인 판단 | 현재 README: 미리보기는 macOS/Linux·JDK/Android SDK 필요, Windows 미지원 |
| [chrisbanes/skills](https://github.com/chrisbanes/skills) | Android, Kotlin · Skill | Kotlin·Compose·Android 개발 스킬 | 원본별 지원 범위 확인 |
| [equinor/design-engineering-skills](https://github.com/equinor/design-engineering-skills) | Web · Skill | 타이포·색·간격·디자인 시스템 지침 | 조직 디자인 전제 확인 |
| [hamen/compose_skill](https://github.com/hamen/compose_skill) | Android · Skill | Compose UI 검토·개발·모션 스킬 | 에이전트 지침이며 Android 라이브러리는 아님 |
| [Leonxlnx/imagegen-skills](https://github.com/Leonxlnx/imagegen-skills) | Web, Mobile · Skill | 이미지 기반 프론트엔드·모바일 디자인·브랜드 작업 지침 | 이미지 생성 도구·프로바이더 요구 확인 |
| [Leonxlnx/taste-skill-classics](https://github.com/Leonxlnx/taste-skill-classics) | Web · Skill | 이전 Taste 스타일별 디자인 스킬 | 현재 taste-skill에서 분리된 스킬; 필요한 것만 선택 |
| [maxgorriaran/react-native-expo-agent-skills](https://github.com/maxgorriaran/react-native-expo-agent-skills) | React Native, Android · Skill | React Native·Expo 개발·QA 스킬 | 작업별 스킬 선택 |
| [plainspace/devour-skills](https://github.com/plainspace/devour-skills) | Web · Skill | 디자인 엔지니어링 검토·비평 지침 | 기존 스킬과 충돌하는 규칙은 프로젝트 기준으로 조정 |
| [Sergio-CVM00/android-design-skills](https://github.com/Sergio-CVM00/android-design-skills) | Android · Skill | Android 적응형 레이아웃·인터랙션 디자인 스킬 | 커뮤니티 지침; 공식 Android 스킬과 구분 |
| [tawhidmonowar/android-design-skills](https://github.com/tawhidmonowar/android-design-skills) | Android · Skill | Compose UI·레이아웃 중심 디자인 스킬 | 커뮤니티 지침·출처 확인 |
| [Uxcel-Lab/product-skills](https://github.com/Uxcel-Lab/product-skills) | Web, Mobile · Skill | UX·제품 설계·제품 관리 지침 | 구현 코드보다 제품 판단 중심 |
| [vercel-labs/skills](https://github.com/vercel-labs/skills) | Web, Mobile · Tool | 에이전트 스킬 검색·추가·관리 CLI | 디자인 스킬 자체와 구분 |
| [zhanziyang/react-native-design-engineering-skill](https://github.com/zhanziyang/react-native-design-engineering-skill) | React Native, Android · Skill | Expo·React Native 터치·모션·디자인 검토 | 네이티브 Compose용과 구분 |

[분야 목록으로](#분야별-바로가기)

<a id="sector-react-ui"></a>

### React · 웹 UI 컴포넌트 · 17개

React 기반 컴포넌트와 접근성 프리미티브. 일부 컴포넌트·템플릿·서비스는 유료일 수 있습니다.

| 프로젝트 | 플랫폼 · 종류 | 무엇에 쓰나 | 적용 메모 |
|---|---|---|---|
| [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) ★ | React, Web · UI | 인터랙티브·애니메이션 React 컴포넌트 | 효과 선택적으로 사용 |
| [mantinedev/mantine](https://github.com/mantinedev/mantine) ★ | React, Web · UI | 폼·훅·컴포넌트가 풍부한 React UI | 앱형 대시보드 후보 |
| [radix-ui/primitives](https://github.com/radix-ui/primitives) ★ | React, Web · UI | 접근성·키보드 상호작용 중심 UI 프리미티브 | 스타일 직접 구성 |
| [shadcn-ui/ui](https://github.com/shadcn-ui/ui) ★ | React, Web · UI | 복사해 수정하는 React 컴포넌트·디자인 시스템 | 기본 UI 구성 첫 후보 |
| [adobe/react-spectrum](https://github.com/adobe/react-spectrum) | React, Web · UI | React Aria·Spectrum 접근성 컴포넌트 | 헤드리스와 디자인 시스템 구분 |
| [ant-design/ant-design](https://github.com/ant-design/ant-design) | React, Web · UI | 관리자·업무 시스템용 React UI | 대시보드·복잡한 폼에 적합 |
| [ariakit/ariakit](https://github.com/ariakit/ariakit) | React, Web · UI | 접근성 중심 React 툴킷 | 복잡한 메뉴·다이얼로그 참고 |
| [chakra-ui/chakra-ui](https://github.com/chakra-ui/chakra-ui) | React, Web · UI | 스타일링과 접근성을 고려한 React 컴포넌트 | 주요 버전 API 차이 확인 |
| [cosscom/ui](https://github.com/cosscom/ui) | React, Web · UI | Cal.com의 coss UI 디자인 시스템 | Origin UI 이전 경로에서 이동; 현재 컴포넌트·라이선스 확인 |
| [daisyui/react-daisyui](https://github.com/daisyui/react-daisyui) | React, Web · UI | daisyUI용 React 컴포넌트 | 원본 daisyUI 버전 호환 확인 |
| [heroui-inc/heroui](https://github.com/heroui-inc/heroui) | React, Web · UI | React UI·테마 컴포넌트 | NextUI 후속 명칭; 버전 확인 |
| [magicuidesign/magicui](https://github.com/magicuidesign/magicui) | React, Web · UI | 랜딩·인터랙션용 모션 컴포넌트 | 공개 라이브러리와 유료 상품 구분 |
| [mui/base-ui](https://github.com/mui/base-ui) | React, Web · UI | 헤드리스 React 컴포넌트 | 프로젝트 스타일 시스템과 결합 |
| [mui/material-ui](https://github.com/mui/material-ui) | React, Web · UI | Material Design React 컴포넌트 | Android Compose와 다른 웹 라이브러리 |
| [radix-ui/themes](https://github.com/radix-ui/themes) | React, Web · UI | Radix 기반 일관된 테마·UI 컴포넌트 | Primitives와 역할 구분 |
| [tailwindlabs/headlessui](https://github.com/tailwindlabs/headlessui) | React, Vue, Web · UI | 스타일 없는 접근성 UI 컴포넌트 | 직접 시각 디자인 필요 |
| [tremorlabs/tremor](https://github.com/tremorlabs/tremor) | React, Web · UI | 대시보드·차트 중심 UI | 템플릿·서비스 라이선스 구분 |

[분야 목록으로](#분야별-바로가기)

<a id="sector-vue-svelte"></a>

### Vue · Svelte · 기타 웹 UI · 11개

React 외 프레임워크용 UI와 디자인 시스템.

| 프로젝트 | 플랫폼 · 종류 | 무엇에 쓰나 | 적용 메모 |
|---|---|---|---|
| [element-plus/element-plus](https://github.com/element-plus/element-plus) | Vue, Web · UI | Vue 3 업무용 UI | 관리자 페이지 후보 |
| [huntabyte/bits-ui](https://github.com/huntabyte/bits-ui) | Svelte, Web · UI | Svelte 헤드리스 컴포넌트 | 키보드·접근성 상태 참고 |
| [huntabyte/shadcn-svelte](https://github.com/huntabyte/shadcn-svelte) | Svelte, Web · UI | Svelte용 shadcn 컴포넌트 | React 버전과 구분 |
| [nuxt/ui](https://github.com/nuxt/ui) | Vue, Nuxt, Web · UI | Nuxt·Vue UI 컴포넌트 | Pro 템플릿 조건과 구분 |
| [primefaces/primevue](https://github.com/primefaces/primevue) | Vue, Web · UI | Vue 컴포넌트·테마 | 일부 템플릿 유료 |
| [quasarframework/quasar](https://github.com/quasarframework/quasar) | Vue, Web, Android · Framework | Vue 기반 웹·모바일 앱 프레임워크 | Android는 Capacitor 등 빌드 경로 확인 |
| [skeletonlabs/skeleton](https://github.com/skeletonlabs/skeleton) | Svelte, Web · UI | Svelte·Tailwind UI 툴킷 | 주요 버전별 지원 스택 확인 |
| [tusen-ai/naive-ui](https://github.com/tusen-ai/naive-ui) | Vue, Web · UI | TypeScript 기반 Vue 3 컴포넌트 | Vue 프로젝트용 |
| [unovue/reka-ui](https://github.com/unovue/reka-ui) | Vue, Web · UI | Vue용 헤드리스 접근성 컴포넌트 | Radix Vue 후속 명칭 확인 |
| [unovue/shadcn-vue](https://github.com/unovue/shadcn-vue) | Vue, Web · UI | Vue용 shadcn 스타일 컴포넌트 | React 코드와 직접 혼용 불가 |
| [vuetifyjs/vuetify](https://github.com/vuetifyjs/vuetify) | Vue, Web · UI | Vue Material Design UI | 버전별 Vue 호환 확인 |

[분야 목록으로](#분야별-바로가기)

<a id="sector-css"></a>

### CSS · 스타일 · 디자인 토큰 · 8개

레이아웃·반응형·디자인 토큰을 구성하는 기반 도구.

| 프로젝트 | 플랫폼 · 종류 | 무엇에 쓰나 | 적용 메모 |
|---|---|---|---|
| [style-dictionary/style-dictionary](https://github.com/style-dictionary/style-dictionary) ★ | Web, Android · Tool | 디자인 토큰을 여러 플랫폼 형식으로 변환 | 웹·Android 색/간격 토큰 공유 |
| [tailwindlabs/tailwindcss](https://github.com/tailwindlabs/tailwindcss) ★ | Web · CSS | 유틸리티 기반 CSS | 반응형·일관된 간격 시스템 |
| [jgthms/bulma](https://github.com/jgthms/bulma) | Web · CSS | CSS 중심 웹 UI 프레임워크 | JavaScript 동작 별도 |
| [picocss/pico](https://github.com/picocss/pico) **보관됨** | Web · CSS | 작고 간단한 의미 기반 CSS | 보관됨(archived): 신규 도입보다 기존 코드 참고용. 작은 문서·도구 페이지에 적합 |
| [saadeghi/daisyui](https://github.com/saadeghi/daisyui) | Web · CSS | Tailwind용 테마·컴포넌트 CSS | 프레임워크 바인딩 없이 사용 가능 |
| [twbs/bootstrap](https://github.com/twbs/bootstrap) | Web · CSS | 반응형 웹 CSS·컴포넌트 | 기성 스타일 기반 |
| [unocss/unocss](https://github.com/unocss/unocss) | Web · CSS | 온디맨드 원자적 CSS 엔진 | 프리셋 설정 필요 |
| [vanilla-extract-css/vanilla-extract](https://github.com/vanilla-extract-css/vanilla-extract) | Web · CSS | TypeScript 기반 정적 CSS·토큰 | 빌드 도구 연결 필요 |

[분야 목록으로](#분야별-바로가기)

<a id="sector-motion"></a>

### 애니메이션 · 스크롤 · 3D · 11개

사용 목적과 성능·reduced-motion 지원을 고려해 선택합니다.

| 프로젝트 | 플랫폼 · 종류 | 무엇에 쓰나 | 적용 메모 |
|---|---|---|---|
| [motiondivision/motion](https://github.com/motiondivision/motion) ★ | React, Web · Motion | React·JavaScript UI 애니메이션 | 레이아웃·상태 변화 모션 |
| [airbnb/lottie-web](https://github.com/airbnb/lottie-web) | Web · Motion | Lottie 벡터 애니메이션 웹 플레이어 | 애니메이션 에셋 라이선스 별도 |
| [darkroomengineering/lenis](https://github.com/darkroomengineering/lenis) | Web · Motion | 부드러운 스크롤 제어 | 키보드·접근성·모션 감소 점검 |
| [formkit/auto-animate](https://github.com/formkit/auto-animate) | Web · Motion | 요소 추가·삭제·재배치 자동 애니메이션 | 간단한 목록·폼 인터랙션 |
| [greensock/GSAP](https://github.com/greensock/GSAP) | Web · Motion | 타임라인·스크롤 애니메이션 | 현재 라이선스·플러그인 조건 확인 |
| [juliangarnier/anime](https://github.com/juliangarnier/anime) | Web · Motion | JavaScript 애니메이션 엔진 | 버전별 API 차이 확인 |
| [mrdoob/three.js](https://github.com/mrdoob/three.js) | Web · 3D | 웹 3D 렌더링 | 렌더링 엔진이며 UI 프레임워크 아님 |
| [pmndrs/drei](https://github.com/pmndrs/drei) | React, Web · 3D | React Three Fiber 보조 컴포넌트 | Three/R3F 버전 호환 확인 |
| [pmndrs/react-spring](https://github.com/pmndrs/react-spring) | React, Web · Motion | 스프링 기반 React 모션 | 상태 기반 상호작용에 적합 |
| [pmndrs/react-three-fiber](https://github.com/pmndrs/react-three-fiber) | React, Web · 3D | React용 Three.js 렌더러 | GPU·모바일 성능 고려 |
| [rive-app/rive-wasm](https://github.com/rive-app/rive-wasm) | Web · Motion | Rive 인터랙티브 애니메이션 웹 런타임 | 편집 서비스·에셋 조건 별도 |

[분야 목록으로](#분야별-바로가기)

<a id="sector-assets"></a>

### 아이콘 · 폰트 · 일러스트 · 10개

코드 라이선스와 폰트·브랜드·개별 에셋 사용 조건은 다를 수 있습니다.

| 프로젝트 | 플랫폼 · 종류 | 무엇에 쓰나 | 적용 메모 |
|---|---|---|---|
| [google/material-design-icons](https://github.com/google/material-design-icons) ★ | Web, Android · Assets | Material 아이콘·심볼 | 웹·Android 디자인 일관성 |
| [lucide-icons/lucide](https://github.com/lucide-icons/lucide) ★ | Web, React Native · Assets | 여러 플랫폼용 선형 아이콘 | 라이선스·패키지 지원 확인 |
| [orioncactus/pretendard](https://github.com/orioncactus/pretendard) ★ | Web, Android · Assets | 한글·라틴 UI용 Pretendard 폰트 | 한국어 앱·웹 타이포 후보 |
| [feathericons/feather](https://github.com/feathericons/feather) | Web · Assets | 간결한 SVG 아이콘 | 가벼운 UI용 |
| [google/fonts](https://github.com/google/fonts) | Web, Android · Assets | 오픈 폰트 컬렉션 | 폰트별 라이선스 확인 |
| [iconify/iconify](https://github.com/iconify/iconify) | Web · Assets | 여러 아이콘 세트를 묶어 쓰는 생태계 | 세트별 라이선스 확인 |
| [phosphor-icons/core](https://github.com/phosphor-icons/core) | Web · Assets | 여러 굵기의 아이콘 원본 | 플랫폼별 바인딩 확인 |
| [simple-icons/simple-icons](https://github.com/simple-icons/simple-icons) | Web · Assets | 브랜드 SVG 아이콘 | 브랜드 상표·가이드 준수 필요 |
| [tabler/tabler-icons](https://github.com/tabler/tabler-icons) | Web · Assets | SVG 아이콘 모음 | 브랜드 아이콘 사용 조건 별도 |
| [tailwindlabs/heroicons](https://github.com/tailwindlabs/heroicons) | Web · Assets | 웹 UI SVG 아이콘 | React·Vue 패키지 제공 |

[분야 목록으로](#분야별-바로가기)

<a id="sector-design-tools"></a>

### 프로토타입 · 디자인 · 문서화 · 8개

설계·다이어그램·디자인 시스템 문서화 도구.

| 프로젝트 | 플랫폼 · 종류 | 무엇에 쓰나 | 적용 메모 |
|---|---|---|---|
| [penpot/penpot](https://github.com/penpot/penpot) ★ | Web · Design | 오픈소스 디자인·프로토타입·협업 도구 | 자체 호스팅·서비스 요구 확인 |
| [storybookjs/storybook](https://github.com/storybookjs/storybook) ★ | Web, React Native · Tool | 컴포넌트 문서·독립 개발·상태 확인 | 디자인 시스템 문서화 |
| [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw) | Web · Design | 손그림 스타일 다이어그램·화이트보드 | UI 자체 설계와 흐름 설명 |
| [figma/code-connect](https://github.com/figma/code-connect) | Web, Android · Tool | Figma 컴포넌트와 코드 연결 | 지원 언어·계정 기능 확인 |
| [mermaid-js/mermaid](https://github.com/mermaid-js/mermaid) | Web · Design | 텍스트 기반 흐름도·아키텍처 그림 | 기획·개발 문서용 |
| [tldraw/tldraw](https://github.com/tldraw/tldraw) | Web · Design | 확장 가능한 캔버스·화이트보드 SDK | SDK 라이선스·배포 조건 확인 |
| [toeverything/AFFiNE](https://github.com/toeverything/AFFiNE) | Web · Design | 문서·화이트보드·기획 협업 | 클라우드와 자체호스팅 기능 차이 |
| [tokens-studio/figma-plugin](https://github.com/tokens-studio/figma-plugin) | Web, Android · Design | Figma 디자인 토큰 관리 플러그인 | 디자인 도구와 코드 토큰 연결 |

[분야 목록으로](#분야별-바로가기)

<a id="sector-charts"></a>

### 차트 · 데이터 화면 · 대시보드 · 11개

일반 차트와 의료·센서 신호 시각화에 참고할 수 있는 라이브러리.

| 프로젝트 | 플랫폼 · 종류 | 무엇에 쓰나 | 적용 메모 |
|---|---|---|---|
| [apache/echarts](https://github.com/apache/echarts) ★ | Web · Charts | 다양한 차트·시각화 | 센서·실험 대시보드 후보 |
| [leeoniya/uPlot](https://github.com/leeoniya/uPlot) ★ | Web · Charts | 가벼운 시계열 차트 | ECG·EMG 시계열 화면 후보 |
| [ag-grid/ag-grid](https://github.com/ag-grid/ag-grid) | Web · UI | 대규모 데이터 그리드 | Community와 Enterprise 라이선스 구분 |
| [airbnb/visx](https://github.com/airbnb/visx) | React, Web · Charts | React용 저수준 시각화 도구 | 개별 시각화 조립용 |
| [chartjs/Chart.js](https://github.com/chartjs/Chart.js) | Web · Charts | Canvas 기반 웹 차트 | 실시간은 데이터 갱신 설계 필요 |
| [d3/d3](https://github.com/d3/d3) | Web · Charts | 맞춤 데이터 시각화 기반 | 자유도 높고 구현량 큼 |
| [gridstack/gridstack.js](https://github.com/gridstack/gridstack.js) | Web · UI | 드래그 가능한 대시보드 격자 | 터치·반응형 검증 |
| [plotly/plotly.js](https://github.com/plotly/plotly.js) | Web · Charts | 과학·통계 인터랙티브 차트 | 번들 크기·성능 확인 |
| [plouc/nivo](https://github.com/plouc/nivo) | React, Web · Charts | React 기반 다양한 차트 | SVG·Canvas 선택 |
| [recharts/recharts](https://github.com/recharts/recharts) | React, Web · Charts | React 차트 컴포넌트 | 간단한 앱형 대시보드 |
| [TanStack/table](https://github.com/TanStack/table) | Web · UI | 헤드리스 데이터 테이블 | 정렬·필터·페이지 처리 |

[분야 목록으로](#분야별-바로가기)

<a id="sector-web-framework"></a>

### 웹 프레임워크 · 앱 기반 · 10개

웹 앱·랜딩·문서 사이트의 프로젝트 기반. Android APK를 직접 만드는 도구는 아닙니다.

| 프로젝트 | 플랫폼 · 종류 | 무엇에 쓰나 | 적용 메모 |
|---|---|---|---|
| [vitejs/vite](https://github.com/vitejs/vite) ★ | Web · Tool | 프론트엔드 개발 서버·빌드 | 작은 웹 도구·카탈로그에 적합 |
| [angular/angular](https://github.com/angular/angular) | Web · Framework | 웹 앱 프레임워크 | TypeScript·구조 중심 |
| [nuxt/nuxt](https://github.com/nuxt/nuxt) | Vue, Web · Framework | Vue 웹 앱 프레임워크 | 배포 모드 선택 |
| [react/react](https://github.com/react/react) | Web · Framework | 컴포넌트 기반 UI 라이브러리 | React Native와 플랫폼 구분 |
| [remix-run/react-router](https://github.com/remix-run/react-router) | React, Web · Framework | React 라우팅·웹 앱 구조 | 모드·메이저 버전 확인 |
| [solidjs/solid](https://github.com/solidjs/solid) | Web · Framework | 반응형 UI 라이브러리 | 생태계·구성 방식 확인 |
| [sveltejs/kit](https://github.com/sveltejs/kit) | Svelte, Web · Framework | Svelte 웹 앱 프레임워크 | 배포 어댑터 확인 |
| [vercel/next.js](https://github.com/vercel/next.js) | React, Web · Framework | React 웹 앱·서버 렌더링 프레임워크 | 웹 프레임워크; APK 직접 생성 아님 |
| [vuejs/core](https://github.com/vuejs/core) | Vue, Web · Framework | Vue UI 프레임워크 | 서드파티 UI 선택 기반 |
| [withastro/astro](https://github.com/withastro/astro) | Web · Framework | 정적 콘텐츠·문서·랜딩 사이트 | 정적 페이지 중심 |

[분야 목록으로](#분야별-바로가기)

<a id="sector-android-samples"></a>

### Android 공식 샘플 · 앱 구조 · 12개

Kotlin·Jetpack·Compose 학습 및 구조 참고. 샘플을 그대로 완성 앱으로 간주하지 않습니다.

| 프로젝트 | 플랫폼 · 종류 | 무엇에 쓰나 | 적용 메모 |
|---|---|---|---|
| [android/camera-samples](https://github.com/android/camera-samples) ★ | Android · Sample | CameraX·Camera2 공식 샘플 | 카메라·사진 앱에 적합 |
| [android/compose-samples](https://github.com/android/compose-samples) ★ | Android · Sample | 공식 Jetpack Compose UI 샘플 | 화면·상태·디자인 구현 참고 |
| [android/nowinandroid](https://github.com/android/nowinandroid) ★ | Android, Kotlin · Sample | 공식 모듈형 Android 앱·Compose 아키텍처 예제 | 구조·오프라인 데이터 흐름 학습 |
| [android/platform-samples](https://github.com/android/platform-samples) ★ | Android · Sample | 카메라·센서·권한 등 Android API 예제 | 기기 기능 연결 참고 |
| [android/architecture-components-samples](https://github.com/android/architecture-components-samples) **보관됨** | Android · Sample | Room·ViewModel 등 Jetpack 구성 예제 | 보관됨(archived): 신규 도입보다 기존 코드 참고용. 오래된 예제의 최신 API 차이 확인 |
| [android/architecture-samples](https://github.com/android/architecture-samples) | Android · Sample | Android 아키텍처·테스트 예제 | 학습용 앱 |
| [android/architecture-templates](https://github.com/android/architecture-templates) | Android · Template | 공식 앱 아키텍처 시작 템플릿 | 현재 지원 템플릿 확인 |
| [android/connectivity-samples](https://github.com/android/connectivity-samples) **보관됨** | Android · Sample | BLE·연결 기능 공식 예제 | 보관됨(archived): 신규 도입보다 기존 코드 참고용. Android 버전별 권한 확인 |
| [android/media-samples](https://github.com/android/media-samples) | Android · Sample | 오디오·영상·미디어 API 샘플 | 앱별 사용 API 확인 |
| [android/permissions-samples](https://github.com/android/permissions-samples) **보관됨** | Android · Sample | 런타임 권한 요청·처리 예제 | 보관됨(archived): 신규 도입보다 기존 코드 참고용. 대상 SDK에 맞춰 적용 |
| [android/user-interface-samples](https://github.com/android/user-interface-samples) **보관됨** | Android · Sample | Android UI·레이아웃·전환 샘플 | 보관됨(archived): 신규 도입보다 기존 코드 참고용. 일부 레거시 Views 예제 |
| [android/wear-os-samples](https://github.com/android/wear-os-samples) | Android, Wear OS · Sample | Wear OS 앱·UI·센서 샘플 | 일반 폰 UI와 구분 |

[분야 목록으로](#분야별-바로가기)

<a id="sector-compose"></a>

### Jetpack Compose UI · 인터랙션 · 13개

네이티브 Android Compose 또는 Compose Multiplatform UI 라이브러리.

| 프로젝트 | 플랫폼 · 종류 | 무엇에 쓰나 | 적용 메모 |
|---|---|---|---|
| [androidx/androidx](https://github.com/androidx/androidx) ★ | Android, Kotlin · Library | Jetpack·Compose AndroidX 라이브러리 원본 | 필요한 모듈 문서부터 |
| [JetBrains/compose-multiplatform](https://github.com/JetBrains/compose-multiplatform) ★ | Android, Kotlin · Framework | Compose UI를 여러 플랫폼에 공유 | Android·데스크톱·기타 지원 확인 |
| [patrykandpatrick/vico](https://github.com/patrykandpatrick/vico) ★ | Android, Kotlin · Charts | Compose Multiplatform용 확장 가능한 차트 | 현재 지원 플랫폼·아티팩트 확인; 이전 Views API와 구분 |
| [airbnb/lottie-android](https://github.com/airbnb/lottie-android) | Android · Motion | Android Lottie 애니메이션 | Compose 연동 패키지·에셋 확인 |
| [Calvin-LL/Reorderable](https://github.com/Calvin-LL/Reorderable) | Android, Kotlin · UI | Compose Multiplatform 목록 재정렬 | 지원 플랫폼 확인 |
| [chrisbanes/haze](https://github.com/chrisbanes/haze) | Android, Kotlin · UI | Compose 배경 블러·유리 효과 | GPU·스크롤 성능 확인 |
| [chrisbanes/tivi](https://github.com/chrisbanes/tivi) **보관됨** | Android, Kotlin · Sample | 실제 Compose 앱 구조·상태·화면 예제 | 보관됨(archived): 신규 도입보다 기존 코드 참고용. 서비스 키·프로젝트 설정 필요 |
| [google/accompanist](https://github.com/google/accompanist) | Android · Library | Compose 보조 라이브러리 모음 | 일부 기능 AndroidX로 이전·폐기; 모듈 상태 확인 |
| [LottieFiles/dotlottie-android](https://github.com/LottieFiles/dotlottie-android) | Android · Motion | dotLottie Android 재생 | 기존 Lottie 런타임과 구분 |
| [PhilJay/MPAndroidChart](https://github.com/PhilJay/MPAndroidChart) | Android · Charts | Android Views 기반 차트 | Compose 전용이 아님; 최신 SDK 호환 점검 |
| [rive-app/rive-android](https://github.com/rive-app/rive-android) | Android · Motion | Android Rive 애니메이션 런타임 | 에셋·편집 도구 조건 확인 |
| [skydoves/Balloon](https://github.com/skydoves/Balloon) | Android · UI | 툴팁·온보딩 팝업 | Compose·Views 지원별 API 확인 |
| [skydoves/landscapist](https://github.com/skydoves/landscapist) | Android · UI | Compose 이미지 로딩·표시 | 로더·Compose 버전 호환 |

[분야 목록으로](#분야별-바로가기)

<a id="sector-android-core"></a>

### Android 데이터 · 네트워크 · 아키텍처 · 15개

Android 앱의 상태·네트워크·직렬화·로컬 데이터·빌드 기반.

| 프로젝트 | 플랫폼 · 종류 | 무엇에 쓰나 | 적용 메모 |
|---|---|---|---|
| [coil-kt/coil](https://github.com/coil-kt/coil) ★ | Android, Kotlin · Library | Kotlin·Compose 이미지 로딩 | 이미지·썸네일 화면 |
| [InsertKoinIO/koin](https://github.com/InsertKoinIO/koin) ★ | Android, Kotlin · Library | Kotlin 의존성 주입 | 작은 앱의 구조화 후보 |
| [Kotlin/kotlinx.coroutines](https://github.com/Kotlin/kotlinx.coroutines) ★ | Android, Kotlin · Library | 비동기 작업·Flow | UI 상태·센서·네트워크 흐름 |
| [lysine-dev/okhttp](https://github.com/lysine-dev/okhttp) ★ | Android, Kotlin · Library | HTTP·WebSocket 네트워크 클라이언트 | 네트워크 기반 |
| [lysine-dev/retrofit](https://github.com/lysine-dev/retrofit) ★ | Android, Kotlin · Library | 타입 기반 HTTP API 클라이언트 | 서버·앱 API 연결 |
| [bumptech/glide](https://github.com/bumptech/glide) | Android · Library | Android 이미지 로딩 | Views 중심 코드와 Compose 연동 구분 |
| [felangel/bloc](https://github.com/felangel/bloc) | Flutter, Android · Library | Dart·Flutter 이벤트·상태 관리 | Riverpod 등과 설계 방식 비교 |
| [google/dagger](https://github.com/google/dagger) | Android, Kotlin · Library | Dagger·Hilt 의존성 주입 | 코드 생성·Gradle 구성 확인 |
| [isar/isar](https://github.com/isar/isar) | Flutter, Android · Library | Dart·Flutter 로컬 데이터베이스 | 유지보수·후속 프로젝트·마이그레이션 검토 |
| [Kotlin/kotlinx.serialization](https://github.com/Kotlin/kotlinx.serialization) | Android, Kotlin · Library | Kotlin 데이터 직렬화 | JSON·서버 스키마 관리 |
| [ktorio/ktor](https://github.com/ktorio/ktor) | Android, Kotlin · Library | Kotlin 네트워크 클라이언트·서버 | 멀티플랫폼 모듈 선택 |
| [rrousselGit/riverpod](https://github.com/rrousselGit/riverpod) | Flutter, Android · Library | Flutter·Dart 상태 관리 | Kotlin Android 라이브러리가 아님 |
| [simolus3/drift](https://github.com/simolus3/drift) | Flutter, Android · Library | Dart·Flutter 반응형 SQL 데이터 계층 | 코드 생성·DB 마이그레이션 필요 |
| [sqldelight/sqldelight](https://github.com/sqldelight/sqldelight) | Android, Kotlin · Library | SQL 기반 타입 안전 DB 코드 생성 | 멀티플랫폼 데이터 계층 후보 |
| [square/moshi](https://github.com/square/moshi) | Android, Kotlin · Library | JSON 파싱·모델 변환 | 직렬화 라이브러리 하나 선택 |

[분야 목록으로](#분야별-바로가기)

<a id="sector-android-device"></a>

### Android 카메라 · BLE · 미디어 · 장치 · 12개

장치 연동은 실제 OS·권한·기기에서 검증해야 합니다.

| 프로젝트 | 플랫폼 · 종류 | 무엇에 쓰나 | 적용 메모 |
|---|---|---|---|
| [androidx/media](https://github.com/androidx/media) ★ | Android · Library | Media3 재생·미디어 처리 | 미디어 앱 기반 |
| [journeyapps/zxing-android-embedded](https://github.com/journeyapps/zxing-android-embedded) ★ | Android · Library | QR·바코드 스캔 | 포토부스 QR 흐름에 활용 |
| [nordicsemi/Android-BLE-Library](https://github.com/nordicsemi/Android-BLE-Library) ★ | Android, Kotlin · Library | BLE 연결·명령·알림 처리 | ESP32·센서·보조장치 앱 후보 |
| [Baseflow/flutter-geolocator](https://github.com/Baseflow/flutter-geolocator) | Flutter, Android · Library | Flutter 위치 조회·위치 스트림 | 위치 권한·백그라운드 정책 확인 |
| [Baseflow/flutter-permission-handler](https://github.com/Baseflow/flutter-permission-handler) | Flutter, Android · Library | Flutter 앱 권한 요청·상태 처리 | Manifest·OS 권한 함께 설정 |
| [dariuszseweryn/RxAndroidBle](https://github.com/dariuszseweryn/RxAndroidBle) | Android · Library | Rx 기반 BLE 통신 | Rx 의존성이 있는 프로젝트용 |
| [flutter/packages](https://github.com/flutter/packages) | Flutter, Android · Library | Flutter 공식 카메라·플랫폼 기능 패키지 모음 | 필요 패키지의 플랫폼별 기능 확인 |
| [fluttercommunity/plus_plugins](https://github.com/fluttercommunity/plus_plugins) | Flutter, Android · Library | 기기·연결·공유 등 Flutter 플러그인 | Android OS별 권한 확인 |
| [google-ai-edge/mediapipe](https://github.com/google-ai-edge/mediapipe) | Android, Web · Library | 손·얼굴·자세 등 인식 파이프라인 | 모델·SDK별 지원 확인 |
| [googlesamples/mlkit](https://github.com/googlesamples/mlkit) | Android · Sample | ML Kit 인식 기능 샘플 | 모델별 온디바이스·클라우드 범위 확인 |
| [mik3y/usb-serial-for-android](https://github.com/mik3y/usb-serial-for-android) | Android · Library | USB 직렬 장치 연결 | USB 호스트·칩셋·권한 확인 |
| [nordicsemi/Kotlin-BLE-Library](https://github.com/nordicsemi/Kotlin-BLE-Library) | Android, Kotlin · Library | Kotlin 기반 BLE API | Android·라이브러리 버전 확인 |

[분야 목록으로](#분야별-바로가기)

<a id="sector-cross-platform"></a>

### React Native · Flutter · 크로스플랫폼 · 10개

Android를 포함한 여러 플랫폼을 목표로 하는 앱 프레임워크.

| 프로젝트 | 플랫폼 · 종류 | 무엇에 쓰나 | 적용 메모 |
|---|---|---|---|
| [expo/expo](https://github.com/expo/expo) ★ | React Native, Android · Framework | React Native 개발·네이티브 모듈·앱 도구 | Expo Go와 설치 APK/AAB 구분 |
| [flutter/flutter](https://github.com/flutter/flutter) ★ | Flutter, Android · Framework | Dart 기반 크로스플랫폼 UI | Android APK 빌드 가능; SDK 필요 |
| [react/react-native](https://github.com/react/react-native) ★ | React Native, Android · Framework | React 기반 네이티브 모바일 앱 | Android 네이티브 빌드 도구 필요 |
| [dotnet/maui](https://github.com/dotnet/maui) | Android · Framework | .NET 기반 멀티플랫폼 앱 | C#·플랫폼별 툴체인 필요 |
| [flet-dev/flet](https://github.com/flet-dev/flet) | Python, Android · Framework | Python 중심 Flutter 기반 앱 UI | 모바일 패키징·지원 패키지 제약 확인 |
| [ionic-team/capacitor](https://github.com/ionic-team/capacitor) | Web, Android · Framework | 웹 앱을 네이티브 앱에 연결하는 런타임 | WebView 기반·권한·플러그인 확인 |
| [ionic-team/ionic-framework](https://github.com/ionic-team/ionic-framework) | Web, Android · UI | 모바일 지향 웹 UI 컴포넌트 | APK는 Capacitor 등과 결합 |
| [kivy/kivy](https://github.com/kivy/kivy) | Python, Android · Framework | Python 기반 터치 UI | APK 빌드·네이티브 외형·패키지 지원 확인 |
| [NativeScript/NativeScript](https://github.com/NativeScript/NativeScript) | Android · Framework | JavaScript·TypeScript 네이티브 앱 개발 | 네이티브 플러그인 지원 확인 |
| [tauri-apps/tauri](https://github.com/tauri-apps/tauri) | Web, Android · Framework | 웹 UI와 네이티브 기능을 연결하는 앱 도구 | 모바일 지원·플러그인 범위 확인 |

[분야 목록으로](#분야별-바로가기)

<a id="sector-mobile-ui"></a>

### 모바일 UI · 탐색 · 모션 · 13개

React Native·Flutter용 UI·애니메이션·내비게이션.

| 프로젝트 | 플랫폼 · 종류 | 무엇에 쓰나 | 적용 메모 |
|---|---|---|---|
| [callstack/react-native-paper](https://github.com/callstack/react-native-paper) ★ | React Native, Android · UI | React Native Material UI | 빠른 앱 화면 구성 |
| [margelo/react-native-vision-camera](https://github.com/margelo/react-native-vision-camera) ★ | React Native, Android · Library | 카메라·프레임 처리 | 권한·실기기·네이티브 빌드 필수 |
| [react-navigation/react-navigation](https://github.com/react-navigation/react-navigation) ★ | React Native, Android · Library | 모바일 화면·탭·스택 탐색 | 내비게이션 기반 |
| [software-mansion/react-native-reanimated](https://github.com/software-mansion/react-native-reanimated) ★ | React Native, Android · Motion | 네이티브 스레드 UI 애니메이션 | Worklets·RN 버전 조합 확인 |
| [flutter-form-builder-ecosystem/flutter_form_builder](https://github.com/flutter-form-builder-ecosystem/flutter_form_builder) | Flutter, Android · UI | Flutter 폼 입력·검증 구성 | 입력 유형별 패키지 확인 |
| [gluestack/gluestack-ui](https://github.com/gluestack/gluestack-ui) | React Native, Web, Android · UI | 웹·네이티브 컴포넌트 | 생성 코드·플랫폼 지원 확인 |
| [gorhom/react-native-bottom-sheet](https://github.com/gorhom/react-native-bottom-sheet) | React Native, Android · UI | 제스처 기반 바텀시트 | 제스처·애니메이션 의존성 필요 |
| [imaNNeo/fl_chart](https://github.com/imaNNeo/fl_chart) | Flutter, Android · Charts | Flutter 선·막대·파이·산점도 등 차트 | 센서·기록 대시보드 후보; Flutter 렌더링 성능 확인 |
| [nativewind/nativewind](https://github.com/nativewind/nativewind) | React Native, Android · CSS | React Native 유틸리티 스타일 | Tailwind·RN 버전 호환 |
| [Shopify/flash-list](https://github.com/Shopify/flash-list) | React Native, Android · UI | 고성능 목록 렌더링 | 목록 크기·아이템 상태 관리 |
| [software-mansion/react-native-gesture-handler](https://github.com/software-mansion/react-native-gesture-handler) | React Native, Android · Library | 터치·제스처 처리 | Reanimated 등과 호환 확인 |
| [tamagui/tamagui](https://github.com/tamagui/tamagui) | React Native, Web, Android · UI | 웹·네이티브 공유 UI·스타일 | 컴파일러·라이선스 범위 확인 |
| [wcandillon/react-native-skia](https://github.com/wcandillon/react-native-skia) | React Native, Android · UI | 네이티브 2D 그래픽·캔버스 | 고급 시각화·렌더링용 |

[분야 목록으로](#분야별-바로가기)

<a id="sector-testing"></a>

### 테스트 · 접근성 · 품질 검사 · 13개

웹·모바일·Android 테스트를 구분합니다. 빌드 성공과 실기기 동작 성공은 다릅니다.

| 프로젝트 | 플랫폼 · 종류 | 무엇에 쓰나 | 적용 메모 |
|---|---|---|---|
| [android/android-test](https://github.com/android/android-test) ★ | Android · Test | AndroidX Test·Espresso 등 테스트 기반 | Android 계측 테스트 |
| [dequelabs/axe-core](https://github.com/dequelabs/axe-core) ★ | Web · Test | 웹 접근성 자동 검사 | 자동 검사만으로 접근성 전체 보장 불가 |
| [microsoft/playwright](https://github.com/microsoft/playwright) ★ | Web · Test | 웹 브라우저·반응형·사용자 흐름 테스트 | Android 네이티브 UI 테스트 아님 |
| [mobile-dev-inc/Maestro](https://github.com/mobile-dev-inc/Maestro) ★ | Android, React Native, Flutter · Test | 모바일 사용자 흐름 자동화 | APK 설치 후 실제 화면 흐름 검사 |
| [appium/appium](https://github.com/appium/appium) | Android, Web · Test | 모바일·웹 자동화 | 드라이버·실기기 설정 필요 |
| [cashapp/paparazzi](https://github.com/cashapp/paparazzi) | Android · Test | Android UI 스크린샷 테스트 | 렌더링·Gradle 버전 확인 |
| [cypress-io/cypress](https://github.com/cypress-io/cypress) | Web · Test | 웹 종단간·컴포넌트 테스트 | 지원 브라우저·구성 확인 |
| [GoogleChrome/lighthouse](https://github.com/GoogleChrome/lighthouse) | Web · Test | 웹 성능·접근성·권장사항 검사 | 실험 환경별 점수 변동 |
| [robolectric/robolectric](https://github.com/robolectric/robolectric) | Android · Test | JVM에서 Android 동작 테스트 | 실기기 UI 검증 대체 아님 |
| [takahirom/roborazzi](https://github.com/takahirom/roborazzi) | Android · Test | Robolectric 기반 스크린샷 테스트 | 시각적 회귀 검사 |
| [testing-library/react-testing-library](https://github.com/testing-library/react-testing-library) | React, Web · Test | 사용자 관점 React 컴포넌트 검사 | 렌더링·접근성 기반 테스트 |
| [vitest-dev/vitest](https://github.com/vitest-dev/vitest) | Web · Test | 프론트엔드 단위·통합 테스트 | 브라우저 테스트와 구분 |
| [wix/Detox](https://github.com/wix/Detox) | React Native, Android · Test | React Native 종단간 테스트 | 앱 빌드·에뮬레이터 설정 필요 |

[분야 목록으로](#분야별-바로가기)

<a id="sector-developer"></a>

### 개발 도구 · 빌드 · API · 릴리스 · 18개

개발·데이터 흐름·모바일 배포·진단 작업을 돕는 도구.

| 프로젝트 | 플랫폼 · 종류 | 무엇에 쓰나 | 적용 메모 |
|---|---|---|---|
| [fastapi/fastapi](https://github.com/fastapi/fastapi) ★ | Python, Web, Android · Framework | 앱·웹용 Python API 서버 | EMG·로봇·센서 백엔드 후보 |
| [square/leakcanary](https://github.com/square/leakcanary) ★ | Android · Tool | Android 메모리 누수 진단 | 디버그 빌드에서 사용 |
| [appwrite/appwrite](https://github.com/appwrite/appwrite) | Web, Android · Backend | 앱 백엔드·인증·DB·스토리지 | 자체 호스팅과 클라우드 구분 |
| [ChuckerTeam/chucker](https://github.com/ChuckerTeam/chucker) | Android · Tool | 앱 내부 HTTP 요청·응답 디버깅 | 민감 데이터 로그·릴리스 포함 여부 확인 |
| [colinhacks/zod](https://github.com/colinhacks/zod) | Web · Library | TypeScript 스키마·데이터 검증 | 클라이언트·서버 계약 검사 |
| [detekt/detekt](https://github.com/detekt/detekt) | Android, Kotlin · Tool | Kotlin 정적 분석 | 품질 규칙 구성 |
| [expo/eas-cli](https://github.com/expo/eas-cli) | React Native, Android · Tool | Expo 앱 빌드·제출·업데이트 CLI | 서비스 계정·요금·서명 설정 확인 |
| [fastlane/fastlane](https://github.com/fastlane/fastlane) | Android · Tool | 모바일 빌드·서명·배포 자동화 | 스토어 계정·서명 비밀 별도 관리 |
| [firebase/flutterfire](https://github.com/firebase/flutterfire) | Flutter, Android · Backend | Flutter용 Firebase 공식 플러그인 | 서비스 계정·클라우드 요금·보안 규칙 확인 |
| [FlutterGen/flutter_gen](https://github.com/FlutterGen/flutter_gen) | Flutter, Android · Tool | Flutter 에셋·폰트 등의 타입 안전 코드 생성 | 코드 생성 단계 필요 |
| [gradle/gradle](https://github.com/gradle/gradle) | Android, Kotlin · Tool | Android·JVM 빌드 자동화 | AGP·JDK 호환 확인 |
| [ktlint/ktlint](https://github.com/ktlint/ktlint) | Android, Kotlin · Tool | Kotlin 코드 스타일 검사 | 자동 포맷 정책 확인 |
| [meta/flipper](https://github.com/meta/flipper) **보관됨** | Android, React Native · Tool | 모바일 앱 디버깅 플랫폼 | 보관됨(archived): 신규 도입보다 기존 코드 참고용. 유지보수·RN 연동 상태 확인 |
| [pmndrs/zustand](https://github.com/pmndrs/zustand) | React, Web · Library | 가벼운 앱 상태 관리 | 서버 상태와 역할 구분 |
| [react-hook-form/react-hook-form](https://github.com/react-hook-form/react-hook-form) | React, Web · Library | React 폼 상태·검증 | 웹 폼에 적합 |
| [supabase/supabase](https://github.com/supabase/supabase) | Web, Android · Backend | DB·인증·스토리지 백엔드 | 호스팅 요금·RLS·앱 키 관리 |
| [TanStack/query](https://github.com/TanStack/query) | Web · Library | 비동기 서버 상태·캐시 관리 | 웹·프레임워크별 바인딩 선택 |
| [vite-pwa/vite-plugin-pwa](https://github.com/vite-pwa/vite-plugin-pwa) | Web · Tool | 웹 앱 PWA 구성 | 설치형 PWA와 네이티브 APK 구분 |

[분야 목록으로](#분야별-바로가기)

<a id="sector-reference"></a>

### 참고 자료 · 패턴 · 모음집 · 9개

추가 탐색을 위한 자료입니다. 개별 라이브러리 항목과 중복 집계하지 않습니다.

| 프로젝트 | 플랫폼 · 종류 | 무엇에 쓰나 | 적용 메모 |
|---|---|---|---|
| [alexpate/awesome-design-systems](https://github.com/alexpate/awesome-design-systems) | Web, Android · Collection | 디자인 시스템 사례·도구 목록 | 시스템별 코드·자산 라이선스 구분 |
| [androiddevnotes/awesome-android-kotlin-apps](https://github.com/androiddevnotes/awesome-android-kotlin-apps) | Android, Kotlin · Collection | Kotlin Android 앱 오픈소스 예제 | 라이브러리와 완성 앱 구분 |
| [brillout/awesome-react-components](https://github.com/brillout/awesome-react-components) | React, Web · Collection | React 컴포넌트 탐색 목록 | 개별 라이브러리 채택 전 검토 |
| [jetpack-compose/jetpack-compose-awesome](https://github.com/jetpack-compose/jetpack-compose-awesome) | Android · Collection | Compose 라이브러리·자료 모음 | 출처별 버전 확인 |
| [jondot/awesome-react-native](https://github.com/jondot/awesome-react-native) | React Native, Android · Collection | React Native 생태계 목록 | 개별 패키지의 현재 지원 확인 |
| [sindresorhus/awesome](https://github.com/sindresorhus/awesome) | Web, Android · Collection | 다양한 분야의 큐레이션 목록 출발점 | 자식 목록은 각각 별도 검토 |
| [Solido/awesome-flutter](https://github.com/Solido/awesome-flutter) | Flutter, Android · Collection | Flutter 라이브러리·샘플 모음 | 개별 의존성·라이선스 확인 |
| [vuejs/awesome-vue](https://github.com/vuejs/awesome-vue) | Vue, Web · Collection | Vue 도구·컴포넌트·프로젝트 모음 | 프레임워크 버전 확인 |
| [wasabeef/awesome-android-ui](https://github.com/wasabeef/awesome-android-ui) | Android · Collection | Android UI 라이브러리 모음 | 오래된 항목·유지보수 상태 확인 |

[분야 목록으로](#분야별-바로가기)

## 출처와 갱신

각 프로젝트 이름은 원본 GitHub 저장소로 연결합니다. 최신성·라이선스·보관 여부·이전 주소·검토 근거는 [JSON](design-app-dev.catalog.json)을 기준으로 다시 확인할 수 있습니다. 원본 프로젝트의 설치 지침은 그 프로젝트의 README를 따릅니다.
