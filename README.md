# Robotics MCP Hub

> **새 모음:** [웹 디자인 · Android · 앱 개발 도구 225개 / 18개 분야](DESIGN_APP_DEV.md) · [검색·필터 HTML](design-app-dev.html)

SO-101 · ROS 2 · Isaac Sim을 포함한 로보틱스 도구 **96개 / 16개 분야** 모음입니다.
기존 47개에 49개를 추가했습니다. 원본 링크·용도·적용 메모를 비교하고 필요한 소스만 내려받을 수 있습니다.

## 시작

Python 3.10 이상과 Git이 필요합니다.

```bash
git clone https://github.com/sangtae03/robotics-mcp-hub.git
cd robotics-mcp-hub
python hub.py sectors
python hub.py list --category gui
python hub.py fetch --category gui --dry-run
python hub.py fetch --category gui
```

Linux에서는 `python3`도 사용할 수 있습니다. Windows `FETCH_RECOMMENDED.cmd`와 Linux `bash fetch-recommended.sh`는 추천 15개 소스를 받습니다.

## 분야별 바로가기

| 분야 | 분류 키 | 개수 |
|---|---|---:|
| [SO-101 · 하드웨어 · 시연 수집](#sector-so101) | `so101` | 12 |
| [설정 · 운영 GUI](#sector-gui) | `gui` | 2 |
| [ROS 2 · 시스템 연결](#sector-ros) | `ros` | 13 |
| [시뮬레이터 MCP · 장면 · 촬영](#sector-sim) | `sim` | 7 |
| [실행 검증 · Action Contract 참고](#sector-safety) | `safety` | 3 |
| [데이터 검수 · 로그 · 시각화](#sector-data) | `data` | 7 |
| [모방학습 · VLA · 정책 평가](#sector-learning) | `learning` | 8 |
| [강화학습 · 사람 개입](#sector-rl) | `rl` | 3 |
| [물리 시뮬레이션 · 데이터 생성 · 벤치마크](#sector-simulation) | `simulation` | 11 |
| [IK · 동역학 · 경로 계획](#sector-control) | `control` | 7 |
| [URDF · 로봇 모델 · 3D 도구](#sector-models) | `models` | 4 |
| [비전 · 점군 · 자세 · 깊이 추정](#sector-vision) | `vision` | 5 |
| [이동로봇 · SLAM · 자율주행](#sector-navigation) | `navigation` | 3 |
| [로봇 에이전트 · 스킬 실행](#sector-agents) | `agents` | 6 |
| [다른 기종의 로봇 MCP](#sector-other) | `other` | 3 |
| [추가 자료 · 모음집](#sector-collections) | `collections` | 2 |

## 선택 다운로드

| 명령 | 동작 |
|---|---|
| `python hub.py sectors` | 분야별 개수와 분류 키 |
| `python hub.py list` | 전체 목록 |
| `python hub.py list --category so101` | SO-101·하드웨어·수집 |
| `python hub.py fetch --category learning --category rl` | 모방학습·VLA와 강화학습 소스 |
| `python hub.py fetch --repo RLinf/RLinf` | 원본 하나 선택 |
| `python hub.py fetch --recommended --dry-run` | 추천 다운로드 계획 |
| `python hub.py fetch --recommended` | 추천 소스 다운로드 |
| `python hub.py fetch --all` | 전체 소스 다운로드 |
| `python hub.py info RLinf/RLinf` | 출처·용도·메모 |
| `python hub.py status` | 받은 소스의 commit·변경 여부 |
| `python hub.py doctor` | Python·Git·ROS 환경 정보 |

기본 경로: `tools/<owner>--<repository>/`. `--dest /원하는/폴더`로 변경할 수 있습니다.
재실행하면 기존 원본 폴더를 건너뛰며 사용자의 수정 내용을 덮어쓰지 않습니다.
이전 분류 키 `support`, `analysis`도 해당 기존 항목을 선택하는 별칭으로 지원합니다.

## 먼저 살펴볼 순서

- 실물 설정·점검: **LeLab → LeStudio → soarm-doctor**
- 기록·품질 분석: **Rerun → Episode Scoring → Pareto**
- SO-101 시뮬레이션: **LeIsaac**
- 학습·평가 확장: **RLinf → OpenPI → XPolicyLab**
- 자세·경로 계산: **PlaCo / Mink / Pink** 중 사용 환경에 맞는 하나

추천은 검토 우선순위입니다. 전체를 한 환경에 함께 설치한다는 의미가 아닙니다.

## 검토 범위와 날짜

- 검토일: **2026-11-23**. 원본 README·공식 문서와 저장소 메타데이터 기준입니다.
- 새 항목의 `created_at`은 저장소 생성 시각, `pushed_at`은 GitHub API의 최근 push 시각입니다. UTC이며 릴리스일이나 기본 브랜치의 마지막 기능 변경일을 뜻하지 않습니다.
- 추가일과 생성일은 다릅니다. 오래된 기반 도구도 유용성에 따라 포함했습니다.
- SO-101 실물 성공률·성능·안전성·Jetson 호환성을 이 허브에서 실행 검증한 것은 아닙니다.
- 원본 소스 다운로드만 제공합니다. 의존성·체크포인트·LFS 에셋·하위 모듈 설치는 각 프로젝트 절차를 따릅니다.
- ROS 2 배포판·Python·CUDA·Isaac Sim/Isaac Lab 버전과 관절 단위·배열 순서·보정을 각각 확인합니다.
- 기존 Isaac Sim 5.1 환경에는 해당 프로젝트의 호환 버전으로 고정합니다.

## 전체 카탈로그

**★ 추천 / ＋ 이번 확장 49개**. 한 프로젝트는 주 분야 한 곳에만 집계합니다.

<a id="sector-so101"></a>

### SO-101 · 하드웨어 · 시연 수집 · 12개

```bash
python hub.py fetch --category so101 --dry-run
```

| 프로젝트 | 용도 | 적용 메모 |
|---|---|---|
| [SO-101 MCP](https://github.com/Tibe31/so101-mcp) ★<br>`Tibe31/so101-mcp` | LeRobot 보정값을 사용한 관절·그리퍼 제어 | 관절 제한과 작은 이동 단계; 충돌 감지는 별도 |
| [Robot MCP for SO-100/101](https://github.com/IliaLarchenko/robot_MCP) ★<br>`IliaLarchenko/robot_MCP` | SO-100/101 제어·카메라·키보드·LLM 예제 | 사용 중인 LeRobot 버전과 API를 확인 |
| [SO-101 ROS MCP on Jetson](https://github.com/itsbharatj/so101_ros_mcp)<br>`itsbharatj/so101_ros_mcp` | Jetson·LeRobot·ROS·MoveIt·MCP 통합 | ROS 2 Humble 기반; Jazzy 포팅 확인 |
| [SO-101 ROS MCP Plugin](https://github.com/anshuman-dev/ros-mcp-plugin)<br>`anshuman-dev/ros-mcp-plugin` | SO-101용 MCP와 ROS 2 Jazzy 브리지 | 기존 joint 명칭·단위·그리퍼 표현에 맞춘 연결 필요 |
| [phospho MCP](https://github.com/phospho-app/phospho-mcp-server)<br>`phospho-app/phospho-mcp-server` | 카메라 조회와 기록된 로봇 동작 재생 | phosphobot 백엔드 필요 |
| [ReflexOS](https://github.com/koikar/cygnus)<br>`koikar/cygnus` | SO-101 관찰·FK/IK·동작 저장·복구 실험 | 개발 중인 프로젝트; 환경별 검증 필요 |
| [LeRobot SO-101 with llama.cpp](https://github.com/hnguyen2402/lerobot-so-101-mcp)<br>`hnguyen2402/lerobot-so-101-mcp` | SO-101 MCP를 로컬 llama.cpp와 연결 | IliaLarchenko/robot_MCP 기반 확장 |
| [SO-100 / SO-101 Hardware](https://github.com/TheRobotStudio/SO-ARM100)<br>`TheRobotStudio/SO-ARM100` | 하드웨어 원본·조립·부품·모터 자료 | 리더·팔로워 하드웨어 자료 |
| [SO-101 ROS2](https://github.com/adoodevv/so101_ros2) ★<br>`adoodevv/so101_ros2` | Jazzy용 URDF·MoveIt·Gazebo·실물 드라이버·리더 조작 | 기존 LeRobot 보정 사용; 원본 설정 절차 확인 |
| [phosphobot](https://github.com/phospho-app/phosphobot)<br>`phospho-app/phosphobot` | SO-101 조작·보정·데이터 기록·학습 UI/API | phospho MCP의 백엔드 |
| [Universal Manipulation Interface](https://github.com/real-stanford/universal_manipulation_interface) ＋<br>`real-stanford/universal_manipulation_interface` | 손에 든 그리퍼로 시연 수집·SLAM·정책 실행 | SO-101 전용이 아님; 별도 UMI 하드웨어와 로봇 연결 필요 |
| [soarm-doctor](https://github.com/shivakumar-sridhar/soarm-doctor) ＋<br>`shivakumar-sridhar/soarm-doctor` | SO-100/101 USB·서보·전원·통신 오류 진단 | README 진단 기능 기준; 실제 고장 원인 최종 확인 필요 |

[분야 목록으로](#분야별-바로가기)

<a id="sector-gui"></a>

### 설정 · 운영 GUI · 2개

```bash
python hub.py fetch --category gui --dry-run
```

| 프로젝트 | 용도 | 적용 메모 |
|---|---|---|
| [LeLab](https://github.com/huggingface/leLab) ★ ＋<br>`huggingface/leLab` | LeRobot 공식 웹 GUI: 보정·텔레옵·수집·학습·재생 | LeRobot 버전·카메라·USB 설정 확인 |
| [LeStudio](https://github.com/TheMomentLab/LeStudio) ★ ＋<br>`TheMomentLab/LeStudio` | USB 포트 매핑·모터 ID·모터 상태·보정 검사 | 하드웨어 진단 중심; 플랫폼별 지원 확인 |

[분야 목록으로](#분야별-바로가기)

<a id="sector-ros"></a>

### ROS 2 · 시스템 연결 · 13개

```bash
python hub.py fetch --category ros --dry-run
```

| 프로젝트 | 용도 | 적용 메모 |
|---|---|---|
| [ROS MCP Server](https://github.com/robotmcp/ros-mcp-server) ★<br>`robotmcp/ros-mcp-server` | rosbridge를 통한 ROS 1/2 토픽·서비스·액션·파라미터 연결 | 로봇 측 rosbridge 실행 필요 |
| [ROS2 MCP](https://github.com/wise-vision/ros2_mcp) ★<br>`wise-vision/ros2_mcp` | rclpy로 ROS 2 그래프에 직접 연결 | ROS 2 환경과 Python 호환성 확인 |
| [LCAS ROS2 MCP](https://github.com/LCAS/ros2_mcp)<br>`LCAS/ros2_mcp` | 토픽·노드 분석과 VLM용 이미지 조회 | cv_bridge 등 ROS 이미지 의존성 확인 |
| [ROS MCP](https://github.com/Yutarop/ros-mcp)<br>`Yutarop/ros-mcp` | ROS 토픽·서비스·액션과 개발 도구 연결 | ROS_DOMAIN_ID와 실행 환경 확인 |
| [Amazing ROS2 MCP](https://github.com/proxi666/amazing-ros2-mcp)<br>`proxi666/amazing-ros2-mcp` | 커스텀 메시지·이미지·Nav2를 포함한 rclpy 기반 연결 | 쓰기 제한은 실제 프로젝트에 맞게 검토 |
| [MoveIt2 MCP](https://github.com/gtoff/moveit-mcp-server)<br>`gtoff/moveit-mcp-server` | FK/IK·경로 계획·충돌 검사·궤적 실행 | 로봇별 MoveIt 설정과 컨트롤러 필요 |
| [Nav2 MCP](https://github.com/ajtudela/nav2_mcp_server)<br>`ajtudela/nav2_mcp_server` | 목적지·경유점·costmap·lifecycle 관리 | 이동로봇용 |
| [Antigravity Robotics Plugin](https://github.com/EngineerAbdullahBinZafar/antigravity-robotics-plugin)<br>`EngineerAbdullahBinZafar/antigravity-robotics-plugin` | ROS 진단·파라미터·대시보드 예제 | SO-101 JointState 연결과 실제 실행 검증 추가 필요 |
| [ROS MCP Demos](https://github.com/robotmcp/demos-ros-mcp-server)<br>`robotmcp/demos-ros-mcp-server` | Gazebo·로봇·드론 연결 데모와 튜토리얼 | 각 하위 예제 README를 따름 |
| [LeRobot ROS](https://github.com/sacovo/lerobot_ros) ★<br>`sacovo/lerobot_ros` | ROS 토픽을 데이터 수집과 정책 실행에 연결 | ROS와 LeRobot Python 환경 호환성 확인 |
| [rosbridge_suite](https://github.com/RobotWebTools/rosbridge_suite)<br>`RobotWebTools/rosbridge_suite` | ROS JSON·WebSocket 인터페이스 | ROS-MCP Server 등과 연결 |
| [ros2_control](https://github.com/ros-controls/ros2_control) ＋<br>`ros-controls/ros2_control` | ROS 2 하드웨어·컨트롤러 통합 | 하드웨어 플러그인과 배포판별 브랜치 확인 |
| [Dora](https://github.com/dora-rs/dora) ＋<br>`dora-rs/dora` | 카메라·AI·제어 모듈의 분산 데이터 흐름 구성 | 기존 ROS 2와의 연결은 별도 설계 |

[분야 목록으로](#분야별-바로가기)

<a id="sector-sim"></a>

### 시뮬레이터 MCP · 장면 · 촬영 · 7개

```bash
python hub.py fetch --category sim --dry-run
```

| 프로젝트 | 용도 | 적용 메모 |
|---|---|---|
| [Isaac Sim MCP Server](https://github.com/whats2000/isaacsim-mcp-server) ★<br>`whats2000/isaacsim-mcp-server` | Isaac Sim 장면·로봇·센서·시뮬레이션 조작 | README 기준 Isaac Sim 5.1.0–6.0.1 대응 |
| [GenRobo Isaac Sim MCP](https://github.com/GenRobo/isaac-sim-mcp)<br>`GenRobo/isaac-sim-mcp` | 관절 제어·재생·스텝·로그·Python 실행 | README에 Isaac Sim 5.1 테스트 명시 |
| [Omni MCP Isaac Sim](https://github.com/omni-mcp/isaac-sim-mcp)<br>`omni-mcp/isaac-sim-mcp` | 장면·조명·로봇 배치·시뮬레이션 조작 | 구버전 기반; Isaac Sim API 호환성 확인 |
| [NVIDIA Kit USD Agents](https://github.com/NVIDIA-Omniverse/kit-usd-agents)<br>`NVIDIA-Omniverse/kit-usd-agents` | Isaac Sim·USD·Kit·OmniUI 문서와 예제 검색 | 문서 검색용 MCP; 시뮬레이터 조작과 구분 |
| [MuJoCo MCP Server](https://github.com/Rongxuan-Zhou/mujoco-mcp-server)<br>`Rongxuan-Zhou/mujoco-mcp-server` | 모델 로드·물리 실행·접촉 분석·궤적 실험 | MuJoCo 환경 필요; README 기능 설명 기준 |
| [SimScene](https://github.com/ros-claw/simscene) ＋<br>`ros-claw/simscene` | 에셋 탐색·USD 장면 구성·Isaac 실행·촬영 | 개발 릴리스; 에셋 라이선스와 물리 검증 필요 |
| [dex-isaac-mcp](https://github.com/Milokucia/dex-isaac-mcp) ＋<br>`Milokucia/dex-isaac-mcp` | 지속 Isaac 세션·관절/게인 조정·시험·캡처·학습 제어 | Docker·USD 로봇 설정·실행 환경 확인 |

[분야 목록으로](#분야별-바로가기)

<a id="sector-safety"></a>

### 실행 검증 · Action Contract 참고 · 3개

```bash
python hub.py fetch --category safety --dry-run
```

| 프로젝트 | 용도 | 적용 메모 |
|---|---|---|
| [Armguard MCP](https://github.com/Lynn-hh/armguard-mcp)<br>`Lynn-hh/armguard-mcp` | 서버 측 관절·공간·속도 제한과 실행 승인·감사 로그 | 알파; README에 실물 로봇 미검증 명시 |
| [ROS2 Manipulator MCP](https://github.com/vagotec/ros2_manipulator_mcp)<br>`vagotec/ros2_manipulator_mcp` | 계획·검증·실행·취소를 분리한 매니퓰레이터 API | ROS 2 Jazzy·MoveIt 어댑터; 기본 실행 비활성화 |
| [MJLab MCP Server](https://github.com/ros-claw/mjlab-mcp-server)<br>`ros-claw/mjlab-mcp-server` | MuJoCo에서 실행 전 궤적 검사를 수행하는 구조 | Action Contract 설계 참고; 실물 안전성 보증 아님 |

[분야 목록으로](#분야별-바로가기)

<a id="sector-data"></a>

### 데이터 검수 · 로그 · 시각화 · 7개

```bash
python hub.py fetch --category data --dry-run
```

| 프로젝트 | 용도 | 적용 메모 |
|---|---|---|
| [Bagel](https://github.com/Extelligence-ai/bagel)<br>`Extelligence-ai/bagel` | ROS bag·MCAP·ROS 로그 등의 자연어 조회·분석 | 지원 포맷과 데이터 경로 확인 |
| [MCP ROS Bags](https://github.com/binabik-ai/mcp-rosbags)<br>`binabik-ai/mcp-rosbags` | 기록된 토픽·궤적·이미지·TF·로그 분석 | ROS 1/2 녹화 데이터 분석 |
| [MCP ROS2 Logs](https://github.com/spanchal001/mcp-ros2-logs)<br>`spanchal001/mcp-ros2-logs` | 여러 노드의 로그를 시간순으로 통합하고 검색 | 로그 파일 분석; ROS 설치 없이 사용 가능 |
| [Rerun](https://github.com/rerun-io/rerun) ★ ＋<br>`rerun-io/rerun` | 영상·관절·좌표계·점군을 동기화해 기록·조회·시각화 | 기존 NPZ·영상 로깅 연결 코드 필요 |
| [LeRobot Episode Scoring](https://github.com/RoboticsData/score_lerobot_episodes) ★ ＋<br>`RoboticsData/score_lerobot_episodes` | 흐림·노출·운동 품질 등 시연 에피소드 점수화 | VLM 평가는 선택 사항; 점수와 실제 성공률 구분 |
| [Pareto](https://github.com/Hebbian-Robotics/pareto) ★ ＋<br>`Hebbian-Robotics/pareto` | LeRobot 시연 일관성·중복·이상 구간 분석·검색·선별 | 자체 호스팅 가능; 색인·모델 의존성 확인 |
| [MCAP](https://github.com/foxglove/mcap) ＋<br>`foxglove/mcap` | 로봇 메시지·센서 로그 저장 형식·라이브러리 | NPZ를 자동 변환하지 않음; 기록 스키마 설계 필요 |

[분야 목록으로](#분야별-바로가기)

<a id="sector-learning"></a>

### 모방학습 · VLA · 정책 평가 · 8개

```bash
python hub.py fetch --category learning --dry-run
```

| 프로젝트 | 용도 | 적용 메모 |
|---|---|---|
| [LeRobot](https://github.com/huggingface/lerobot)<br>`huggingface/lerobot` | SO-101 보정·조작·데이터 수집·정책 학습·추론 | 로봇 학습과 제어 기반 |
| [Isaac GR00T](https://github.com/NVIDIA/Isaac-GR00T)<br>`NVIDIA/Isaac-GR00T` | VLA 데이터 형식·미세조정·추론 | 사용 중인 N1.6과 최신 main의 차이 확인 |
| [XPolicyLab](https://github.com/XPolicyLab/XPolicyLab) ★ ＋<br>`XPolicyLab/XPolicyLab` | 정책 서버·관측/행동 계약·벤치마크 평가 통합 | 모델별 환경·체크포인트·어댑터 설정 필요 |
| [OpenPI](https://github.com/Physical-Intelligence/openpi) ＋<br>`Physical-Intelligence/openpi` | π₀·π₀-FAST·π₀.₅ 추론·미세조정 | SO-101 데이터·행동 공간 연결과 GPU 자원 필요 |
| [OpenVLA](https://github.com/openvla/openvla) ＋<br>`openvla/openvla` | 공개 VLA 추론·LoRA 미세조정 | 원본과 OFT 구분; 데이터/행동 어댑터 필요 |
| [Octo](https://github.com/octo-models/octo) ＋<br>`octo-models/octo` | 범용 로봇 정책 추론·미세조정 | 로봇별 관측·행동 공간 및 의존성 확인 |
| [Diffusion Policy](https://github.com/real-stanford/diffusion_policy) ＋<br>`real-stanford/diffusion_policy` | 영상·상태 기반 동작 시퀀스 학습 | 기존 BC 비교용; 데이터 변환·환경 구현 필요 |
| [robomimic](https://github.com/ARISE-Initiative/robomimic) ＋<br>`ARISE-Initiative/robomimic` | 시연 기반 학습·오프라인 알고리즘·재현 실험 | 기존 NPZ를 학습 형식으로 변환해야 함 |

[분야 목록으로](#분야별-바로가기)

<a id="sector-rl"></a>

### 강화학습 · 사람 개입 · 3개

```bash
python hub.py fetch --category rl --dry-run
```

| 프로젝트 | 용도 | 적용 메모 |
|---|---|---|
| [HIL-SERL](https://github.com/rail-berkeley/hil-serl)<br>`rail-berkeley/hil-serl` | 시연·사람 개입을 사용하는 실물 강화학습 | Franka 예제 중심; SO-101 환경 구현 필요 |
| [RLinf](https://github.com/RLinf/RLinf) ★ ＋<br>`RLinf/RLinf` | 로봇 강화학습·SO-101 시연 수집·OpenPI 미세조정·평가 | SO-101 전용 절차와 연산 자원 요구 확인 |
| [gym-hil](https://github.com/huggingface/gym-hil) ＋<br>`huggingface/gym-hil` | 사람 개입을 지원하는 Gymnasium 강화학습 환경 | 현재 README는 Franka 환경 중심; SO-101 환경 구현 필요 |

[분야 목록으로](#분야별-바로가기)

<a id="sector-simulation"></a>

### 물리 시뮬레이션 · 데이터 생성 · 벤치마크 · 11개

```bash
python hub.py fetch --category simulation --dry-run
```

| 프로젝트 | 용도 | 적용 메모 |
|---|---|---|
| [Isaac Lab](https://github.com/isaac-sim/IsaacLab)<br>`isaac-sim/IsaacLab` | 병렬 시뮬레이션과 강화학습 환경 | Isaac Sim 5.1에는 v2.3.x 계열 대응; main 버전 확인 |
| [LeIsaac](https://github.com/LightwheelAI/leisaac) ★ ＋<br>`LightwheelAI/leisaac` | SO-101 Isaac Lab 텔레옵·시연 수집·데이터 변환·정책 실행 | GR00T N1.6 지원 문서; Isaac Sim/Isaac Lab 조합 확인 |
| [ManiSkill](https://github.com/mani-skill/ManiSkill) ＋<br>`mani-skill/ManiSkill` | GPU 병렬 조작 시뮬레이션·학습·평가 | OS·SAPIEN·GPU 지원과 로봇 모델 확인 |
| [Genesis](https://github.com/Genesis-Embodied-AI/genesis-world) ＋<br>`Genesis-Embodied-AI/genesis-world` | 로봇·강체·연성 물체 등을 위한 물리 시뮬레이션 | 기존 Isaac 환경을 자동 변환하는 도구는 아님 |
| [robosuite](https://github.com/ARISE-Initiative/robosuite) ＋<br>`ARISE-Initiative/robosuite` | MuJoCo 조작 환경·컨트롤러·센서·벤치마크 | SO-101 로봇·작업 환경 구현 필요 |
| [MimicGen](https://github.com/NVlabs/mimicgen) ＋<br>`NVlabs/mimicgen` | 소수 시연 기반 시뮬레이션 데이터 생성 | 작업 분할·물체 좌표·환경 인터페이스 필요 |
| [RoboCasa](https://github.com/robocasa/robocasa) ＋<br>`robocasa/robocasa` | 생활·주방 조작 작업·장면·시연 데이터·평가 | 대규모 연구 환경; SO-101 즉시 실행 제공으로 해석 금지 |
| [RoboTwin](https://github.com/RoboTwin-Platform/RoboTwin) ＋<br>`RoboTwin-Platform/RoboTwin` | 양팔 조작 데이터 생성·벤치마크 | 기본 로봇·제어 방식과 SO-101 차이 확인 |
| [IsaacLab-Arena](https://github.com/isaac-sim/IsaacLab-Arena) ＋<br>`isaac-sim/IsaacLab-Arena` | 조합 가능한 Isaac Lab 작업 환경·정책 평가 | Isaac 버전과 작업·로봇 어댑터 확인 |
| [RoboDojo](https://github.com/RoboDojo-Benchmark/RoboDojo) ＋<br>`RoboDojo-Benchmark/RoboDojo` | 시뮬·실물 조작 평가 벤치마크 | 현재 릴리스는 평가 중심; 정책 서버는 XPolicyLab |
| [Newton](https://github.com/newton-physics/newton) ＋<br>`newton-physics/newton` | NVIDIA Warp 기반 GPU 물리 시뮬레이션 엔진 | 엔진/연구 기반; 작업·로봇·학습 환경 구성 필요 |

[분야 목록으로](#분야별-바로가기)

<a id="sector-control"></a>

### IK · 동역학 · 경로 계획 · 7개

```bash
python hub.py fetch --category control --dry-run
```

| 프로젝트 | 용도 | 적용 메모 |
|---|---|---|
| [MoveIt2](https://github.com/moveit/moveit2)<br>`moveit/moveit2` | IK·충돌 검사·경로 계획 | ROS 2 조작 계획 기반 |
| [cuRobo](https://github.com/NVlabs/curobo)<br>`NVlabs/curobo` | GPU 기반 IK·충돌 검사·궤적 최적화 | v1/v2 API 변경과 CUDA 의존성 확인 |
| [PlaCo](https://github.com/Rhoban/placo) ＋<br>`Rhoban/placo` | 작업·제약 기반 역기구학·역동역학 | URDF·좌표계·관절 단위 및 제약 설정 필요 |
| [Mink](https://github.com/kevinzakka/mink) ＋<br>`kevinzakka/mink` | MuJoCo 기반 제약 미분 IK | MuJoCo 모델·작업·제한 조건 설정 필요 |
| [Pink](https://github.com/pink-kinematics/pink) ＋<br>`pink-kinematics/pink` | Pinocchio 기반 Python 미분 IK | 관절 제한·목표 작업·QP 설정 필요 |
| [Pinocchio](https://github.com/stack-of-tasks/pinocchio) ＋<br>`stack-of-tasks/pinocchio` | 기구학·Jacobian·동역학·미분 계산 | 라이브러리; 모터 드라이버·경로 계획은 별도 |
| [OMPL](https://github.com/ompl/ompl) ＋<br>`ompl/ompl` | 샘플링 기반 경로 계획 | 충돌 판정·상태 공간·로봇 모델 연결 필요 |

[분야 목록으로](#분야별-바로가기)

<a id="sector-models"></a>

### URDF · 로봇 모델 · 3D 도구 · 4개

```bash
python hub.py fetch --category models --dry-run
```

| 프로젝트 | 용도 | 적용 메모 |
|---|---|---|
| [Viser](https://github.com/viser-project/viser) ＋<br>`viser-project/viser` | Python 웹 3D 시각화·상호작용·GUI | 물리 엔진이 아님; 자세·센서 데이터 연결 필요 |
| [yourdfpy](https://github.com/clemense/yourdfpy) ＋<br>`clemense/yourdfpy` | URDF 읽기·수정·검증·시각화 | 메시 경로·스케일·관절축 점검용 |
| [Robot Descriptions](https://github.com/robot-descriptions/robot_descriptions.py) ＋<br>`robot-descriptions/robot_descriptions.py` | 다양한 로봇 URDF·MJCF 모델 다운로드·로딩 | 모델별 라이선스·지원 로봇 확인 |
| [URDF Studio](https://github.com/OpenLegged/URDF-Studio) ＋<br>`OpenLegged/URDF-Studio` | 웹 로봇 모델 편집·충돌 형상·다중 형식 입출력 | 변환 결과의 관절축·질량·충돌 형상 검증 필요 |

[분야 목록으로](#분야별-바로가기)

<a id="sector-vision"></a>

### 비전 · 점군 · 자세 · 깊이 추정 · 5개

```bash
python hub.py fetch --category vision --dry-run
```

| 프로젝트 | 용도 | 적용 메모 |
|---|---|---|
| [Open3D](https://github.com/isl-org/Open3D) ＋<br>`isl-org/Open3D` | 점군·정합·재구성·3D 시각화 | 깊이 단위·카메라 보정·좌표계 연결 필요 |
| [FoundationPose](https://github.com/NVlabs/FoundationPose) ＋<br>`NVlabs/FoundationPose` | 물체 6D 자세 추정·추적 | CAD 또는 참조 영상·관련 입력 필요; 모델/코드 라이선스 확인 |
| [FoundationStereo](https://github.com/NVlabs/FoundationStereo) ＋<br>`NVlabs/FoundationStereo` | 스테레오 시차·깊이·점군 추정 | 보정된 좌·우 영상 필요; 단안 모델 아님 |
| [Fast-FoundationStereo](https://github.com/NVlabs/Fast-FoundationStereo) ＋<br>`NVlabs/Fast-FoundationStereo` | 실시간 처리를 목표로 하는 스테레오 깊이 추정 | 입력 보정·하드웨어별 속도·라이선스 확인 |
| [SAM 3](https://github.com/facebookresearch/sam3) ＋<br>`facebookresearch/sam3` | 텍스트·시각 프롬프트 기반 물체 분할·추적 | 체크포인트 접근·GPU 자원 확인; 깊이나 로봇 제어는 별도 |

[분야 목록으로](#분야별-바로가기)

<a id="sector-navigation"></a>

### 이동로봇 · SLAM · 자율주행 · 3개

```bash
python hub.py fetch --category navigation --dry-run
```

| 프로젝트 | 용도 | 적용 메모 |
|---|---|---|
| [Nav2](https://github.com/ros-navigation/navigation2) ＋<br>`ros-navigation/navigation2` | ROS 2 이동로봇 경로 계획·자율주행 | 모바일 베이스·센서·TF·제어기 구성 필요 |
| [SLAM Toolbox](https://github.com/SteveMacenski/slam_toolbox) ＋<br>`SteveMacenski/slam_toolbox` | 2D 지도 작성·위치 추정·지속 지도 관리 | LiDAR·TF·오도메트리 연결 필요 |
| [RTAB-Map ROS](https://github.com/introlab/rtabmap_ros) ＋<br>`introlab/rtabmap_ros` | RGB-D·스테레오·LiDAR 기반 SLAM·3D 지도 | 센서 동기화·보정·ROS 배포판 확인 |

[분야 목록으로](#분야별-바로가기)

<a id="sector-agents"></a>

### 로봇 에이전트 · 스킬 실행 · 6개

```bash
python hub.py fetch --category agents --dry-run
```

| 프로젝트 | 용도 | 적용 메모 |
|---|---|---|
| [ROS MCP Client](https://github.com/robotmcp/robotmcp_client)<br>`robotmcp/robotmcp_client` | LLM과 ROS MCP 서버를 잇는 자체 클라이언트 예제 | 서버와 클라이언트 역할 구분 |
| [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)<br>`modelcontextprotocol/python-sdk` | 자체 Python 코드를 MCP 도구로 노출 | 정책 학습 프레임워크와 별개의 인터페이스 |
| [ASPIRE](https://github.com/NVlabs/ASPIRE)<br>`NVlabs/ASPIRE` | 로봇 작업용 코드와 재사용 동작 발견 연구 | 연구용; SO-101 연결은 별도 구현 |
| [DimOS](https://github.com/dimensionalOS/dimos)<br>`dimensionalOS/dimos` | 로봇 인지·동작·에이전트 런타임과 MCP 연동 | 플랫폼 구조 참고; 로봇별 어댑터 확인 |
| [Roboglot / quackd](https://github.com/rokbenko/quackd) ＋<br>`rokbenko/quackd` | LLM·MCP 기반 로봇 스킬 호출·다중 로봇 연결 | README상 SO-101 실물 기록; 다른 로봇은 mock 검증 범위 구분 |
| [AllenAI Agentic Robotics](https://github.com/allenai/agentic_robotics) ＋<br>`allenai/agentic_robotics` | MCP 스킬을 VLM이 호출하는 작업 실행 루프 | 현재 ToyBlocks 중심; 독립 성공 검증기 없음; SO-101 어댑터 별도 |

[분야 목록으로](#분야별-바로가기)

<a id="sector-other"></a>

### 다른 기종의 로봇 MCP · 3개

```bash
python hub.py fetch --category other --dry-run
```

| 프로젝트 | 용도 | 적용 메모 |
|---|---|---|
| [Unitree Go2 MCP](https://github.com/lpigeon/unitree-go2-mcp-server)<br>`lpigeon/unitree-go2-mcp-server` | Go2 자연어 요청을 ROS 2 명령으로 연결 | Unitree Go2용; SO-101 어댑터 제공 아님 |
| [myCobot MCP](https://github.com/neka-nat/mycobot-mcp)<br>`neka-nat/mycobot-mcp` | 이미지 피드백을 이용한 myCobot Pick & Place | myCobot용; 비전 백엔드 설정 필요 |
| [Universal Robots MCP](https://github.com/nonead/Nonead-Universal-Robots-MCP)<br>`nonead/Nonead-Universal-Robots-MCP` | Universal Robots 제어를 연결하는 MCP | 산업용 로봇 연결 설계 참고 |

[분야 목록으로](#분야별-바로가기)

<a id="sector-collections"></a>

### 추가 자료 · 모음집 · 2개

```bash
python hub.py fetch --category collections --dry-run
```

| 프로젝트 | 용도 | 적용 메모 |
|---|---|---|
| [Awesome Hardware Skills](https://github.com/chopinfeng/awesome-hardware-skills)<br>`chopinfeng/awesome-hardware-skills` | 하드웨어 MCP·에이전트 도구·시뮬레이터 모음 | 추가 프로젝트 탐색용 |
| [Awesome Embodied Agents](https://github.com/benchflow-ai/awesome-embodied-agents)<br>`benchflow-ai/awesome-embodied-agents` | 로봇 에이전트·모델·MCP·평가 자료 모음 | 추가 연구와 도구 탐색용 |

[분야 목록으로](#분야별-바로가기)

## 라이선스와 출처

허브 코드·문서는 MIT입니다. 원본 소스·모델·데이터·에셋은 각각의 라이선스를 따릅니다.
API가 `NOASSERTION`을 반환하거나 라이선스가 표시되지 않는 항목을 MIT로 간주하지 않습니다.
원본 실행 코드는 이 저장소에 복사하지 않았습니다. [catalog.json](catalog.json)에 항목별 출처·메타데이터가 있습니다.

## 로컬 검증

```bash
python -m unittest discover -s tests -v
python hub.py sectors
python hub.py fetch --all --dry-run
```
