# Robotics MCP Hub

SO-101 · ROS 2 Jazzy · Isaac Sim 환경에서 참고하고 사용할 로보틱스 도구 **47개**를 모은 개인 허브입니다.

원본 링크와 검토 메모를 한곳에서 찾고, 필요한 소스만 선택하거나 한 번에 내려받을 수 있습니다. 각 도구의 실제 패키지 설치와 로봇 연결은 해당 프로젝트의 절차를 따릅니다.

## 시작

Python 3.10 이상과 Git이 필요합니다.

```bash
git clone https://github.com/sangtae03/robotics-mcp-hub.git
cd robotics-mcp-hub
python hub.py list
python hub.py fetch --recommended
```

Linux에서 `python` 대신 `python3`를 사용할 수 있습니다. Windows에서는 `FETCH_RECOMMENDED.cmd`, Linux에서는 `bash fetch-recommended.sh`도 사용할 수 있습니다.

## 사용 명령

| 명령 | 동작 |
|---|---|
| `python hub.py list` | 47개 목록 |
| `python hub.py list --category so101` | SO-101 항목 |
| `python hub.py info tibe31--so101-mcp` | 원본 README와 연결 메모 |
| `python hub.py fetch --recommended --dry-run` | 다운로드 계획 확인 |
| `python hub.py fetch --recommended` | 우선 추천 7개 소스 다운로드 |
| `python hub.py fetch --category so101` | SO-101 분류 소스 다운로드 |
| `python hub.py fetch --all` | 전체 47개 소스 다운로드 |
| `python hub.py fetch --repo robotmcp/ros-mcp-server` | 원본 하나 선택 |
| `python hub.py status` | 다운로드한 소스의 commit·변경 여부 |
| `python hub.py doctor` | Python·Git·ROS 환경 정보 |

카테고리: `so101`, `ros`, `sim`, `safety`, `analysis`, `other`, `support`, `collections`.

기본 저장 위치는 이 허브 안의 `tools/<owner>--<repository>/`입니다. `--dest /원하는/폴더`로 변경할 수 있습니다. 재실행하면 같은 원본의 기존 폴더를 건너뛰며 수정한 내용을 덮어쓰지 않습니다.

## 환경에서의 사용 순서

1. `doctor`로 Git과 Python을 확인합니다.
2. `fetch --recommended`로 우선 후보의 소스를 받습니다.
3. ROS 2 연결은 `robotmcp/ros-mcp-server` 또는 `wise-vision/ros2_mcp` 중 필요한 구성을 선택합니다.
4. Isaac Sim 조작은 `whats2000/isaacsim-mcp-server`의 5.1 대응 설치 절차를 확인합니다.
5. 기존 정책·데이터 연결은 `sacovo/lerobot_ros`, Jazzy용 SO-101 스택은 `adoodevv/so101_ros2`를 검토합니다.

ROS 2 토픽의 관절 이름·배열 순서·단위·그리퍼 표현과 LeRobot 보정 방식은 기존 제어기에 맞게 연결해야 합니다. 이 허브의 다운로드 명령은 모터 명령을 보내지 않습니다.

## 설치·버전 메모

- 전체 다운로드에는 Python 의존성 설치, 모델 가중치, Git LFS 에셋, 하위 모듈 자동 다운로드가 포함되지 않습니다. 필요한 항목은 각 원본 README를 따릅니다.
- 프로젝트별 가상환경을 사용합니다. ROS의 Python과 Isaac Sim 내부 Python은 역할과 의존성이 다릅니다.
- 검토 시점 Isaac Lab README 기준으로 Isaac Sim **5.1은 v2.3.x 계열**에 대응합니다. 최신 `main`의 호환성은 별도로 확인합니다.
- NVIDIA 공식 Kit/USD Agents의 Isaac Sim MCP는 문서·예제 검색용입니다. 시뮬레이터 조작용 MCP와 역할이 다릅니다.
- 실행 검증·안전 관련 항목의 기능은 원본 README 설명입니다. SO-101 실물 구동 성공이나 안전성을 이 모음에서 검증한 것은 아닙니다.

## 전체 카탈로그

검토일: 2026-11-23. **추천**은 개인 환경에 대한 검토 우선순위이며 호환성 인증을 뜻하지 않습니다.

### SO-101 직접 연결

| 원본 | 용도 | 연결 메모 |
|---|---|---|
| [Tibe31/so101-mcp](https://github.com/Tibe31/so101-mcp) **추천** | LeRobot 보정값을 사용한 관절·그리퍼 제어 | 관절 제한과 작은 이동 단계; 충돌 감지는 별도 |
| [IliaLarchenko/robot_MCP](https://github.com/IliaLarchenko/robot_MCP) **추천** | SO-100/101 제어·카메라·키보드·LLM 예제 | 사용 중인 LeRobot 버전과 API를 확인 |
| [itsbharatj/so101_ros_mcp](https://github.com/itsbharatj/so101_ros_mcp) | Jetson·LeRobot·ROS·MoveIt·MCP 통합 | ROS 2 Humble 기반; Jazzy 포팅 확인 |
| [anshuman-dev/ros-mcp-plugin](https://github.com/anshuman-dev/ros-mcp-plugin) | SO-101용 MCP와 ROS 2 Jazzy 브리지 | 기존 joint 명칭·단위·그리퍼 표현에 맞춘 연결 필요 |
| [phospho-app/phospho-mcp-server](https://github.com/phospho-app/phospho-mcp-server) | 카메라 조회와 기록된 로봇 동작 재생 | phosphobot 백엔드 필요 |
| [koikar/cygnus](https://github.com/koikar/cygnus) | SO-101 관찰·FK/IK·동작 저장·복구 실험 | 개발 중인 프로젝트; 환경별 검증 필요 |
| [hnguyen2402/lerobot-so-101-mcp](https://github.com/hnguyen2402/lerobot-so-101-mcp) | SO-101 MCP를 로컬 llama.cpp와 연결 | IliaLarchenko/robot_MCP 기반 확장 |

### ROS MCP

| 원본 | 용도 | 연결 메모 |
|---|---|---|
| [robotmcp/ros-mcp-server](https://github.com/robotmcp/ros-mcp-server) **추천** | rosbridge를 통한 ROS 1/2 토픽·서비스·액션·파라미터 연결 | 로봇 측 rosbridge 실행 필요 |
| [wise-vision/ros2_mcp](https://github.com/wise-vision/ros2_mcp) **추천** | rclpy로 ROS 2 그래프에 직접 연결 | ROS 2 환경과 Python 호환성 확인 |
| [LCAS/ros2_mcp](https://github.com/LCAS/ros2_mcp) | 토픽·노드 분석과 VLM용 이미지 조회 | cv_bridge 등 ROS 이미지 의존성 확인 |
| [Yutarop/ros-mcp](https://github.com/Yutarop/ros-mcp) | ROS 토픽·서비스·액션과 개발 도구 연결 | ROS_DOMAIN_ID와 실행 환경 확인 |
| [proxi666/amazing-ros2-mcp](https://github.com/proxi666/amazing-ros2-mcp) | 커스텀 메시지·이미지·Nav2를 포함한 rclpy 기반 연결 | 쓰기 제한은 실제 프로젝트에 맞게 검토 |
| [gtoff/moveit-mcp-server](https://github.com/gtoff/moveit-mcp-server) | FK/IK·경로 계획·충돌 검사·궤적 실행 | 로봇별 MoveIt 설정과 컨트롤러 필요 |
| [ajtudela/nav2_mcp_server](https://github.com/ajtudela/nav2_mcp_server) | 목적지·경유점·costmap·lifecycle 관리 | 이동로봇용 |
| [EngineerAbdullahBinZafar/antigravity-robotics-plugin](https://github.com/EngineerAbdullahBinZafar/antigravity-robotics-plugin) | ROS 진단·파라미터·대시보드 예제 | SO-101 JointState 연결과 실제 실행 검증 추가 필요 |

### Isaac Sim / MuJoCo

| 원본 | 용도 | 연결 메모 |
|---|---|---|
| [whats2000/isaacsim-mcp-server](https://github.com/whats2000/isaacsim-mcp-server) **추천** | Isaac Sim 장면·로봇·센서·시뮬레이션 조작 | README 기준 Isaac Sim 5.1.0–6.0.1 대응 |
| [GenRobo/isaac-sim-mcp](https://github.com/GenRobo/isaac-sim-mcp) | 관절 제어·재생·스텝·로그·Python 실행 | README에 Isaac Sim 5.1 테스트 명시 |
| [omni-mcp/isaac-sim-mcp](https://github.com/omni-mcp/isaac-sim-mcp) | 장면·조명·로봇 배치·시뮬레이션 조작 | 구버전 기반; Isaac Sim API 호환성 확인 |
| [NVIDIA-Omniverse/kit-usd-agents](https://github.com/NVIDIA-Omniverse/kit-usd-agents) | Isaac Sim·USD·Kit·OmniUI 문서와 예제 검색 | 문서 검색용 MCP; 시뮬레이터 조작과 구분 |
| [Rongxuan-Zhou/mujoco-mcp-server](https://github.com/Rongxuan-Zhou/mujoco-mcp-server) | 모델 로드·물리 실행·접촉 분석·궤적 실험 | MuJoCo 환경 필요; README 기능 설명 기준 |

### 실행 검증 구조

| 원본 | 용도 | 연결 메모 |
|---|---|---|
| [Lynn-hh/armguard-mcp](https://github.com/Lynn-hh/armguard-mcp) | 서버 측 관절·공간·속도 제한과 실행 승인·감사 로그 | 알파; README에 실물 로봇 미검증 명시 |
| [vagotec/ros2_manipulator_mcp](https://github.com/vagotec/ros2_manipulator_mcp) | 계획·검증·실행·취소를 분리한 매니퓰레이터 API | ROS 2 Jazzy·MoveIt 어댑터; 기본 실행 비활성화 |
| [ros-claw/mjlab-mcp-server](https://github.com/ros-claw/mjlab-mcp-server) | MuJoCo에서 실행 전 궤적 검사를 수행하는 구조 | Action Contract 설계 참고; 실물 안전성 보증 아님 |

### 로그·데이터·연결 예제

| 원본 | 용도 | 연결 메모 |
|---|---|---|
| [Extelligence-ai/bagel](https://github.com/Extelligence-ai/bagel) | ROS bag·MCAP·ROS 로그 등의 자연어 조회·분석 | 지원 포맷과 데이터 경로 확인 |
| [binabik-ai/mcp-rosbags](https://github.com/binabik-ai/mcp-rosbags) | 기록된 토픽·궤적·이미지·TF·로그 분석 | ROS 1/2 녹화 데이터 분석 |
| [spanchal001/mcp-ros2-logs](https://github.com/spanchal001/mcp-ros2-logs) | 여러 노드의 로그를 시간순으로 통합하고 검색 | 로그 파일 분석; ROS 설치 없이 사용 가능 |
| [robotmcp/demos-ros-mcp-server](https://github.com/robotmcp/demos-ros-mcp-server) | Gazebo·로봇·드론 연결 데모와 튜토리얼 | 각 하위 예제 README를 따름 |
| [robotmcp/robotmcp_client](https://github.com/robotmcp/robotmcp_client) | LLM과 ROS MCP 서버를 잇는 자체 클라이언트 예제 | 서버와 클라이언트 역할 구분 |

### 다른 기종의 MCP

| 원본 | 용도 | 연결 메모 |
|---|---|---|
| [lpigeon/unitree-go2-mcp-server](https://github.com/lpigeon/unitree-go2-mcp-server) | Go2 자연어 요청을 ROS 2 명령으로 연결 | Unitree Go2용; SO-101 어댑터 제공 아님 |
| [neka-nat/mycobot-mcp](https://github.com/neka-nat/mycobot-mcp) | 이미지 피드백을 이용한 myCobot Pick & Place | myCobot용; 비전 백엔드 설정 필요 |
| [nonead/Nonead-Universal-Robots-MCP](https://github.com/nonead/Nonead-Universal-Robots-MCP) | Universal Robots 제어를 연결하는 MCP | 산업용 로봇 연결 설계 참고 |

### 학습·제어·개발 기반

| 원본 | 용도 | 연결 메모 |
|---|---|---|
| [huggingface/lerobot](https://github.com/huggingface/lerobot) | SO-101 보정·조작·데이터 수집·정책 학습·추론 | 로봇 학습과 제어 기반 |
| [TheRobotStudio/SO-ARM100](https://github.com/TheRobotStudio/SO-ARM100) | 하드웨어 원본·조립·부품·모터 자료 | 리더·팔로워 하드웨어 자료 |
| [sacovo/lerobot_ros](https://github.com/sacovo/lerobot_ros) **추천** | ROS 토픽을 데이터 수집과 정책 실행에 연결 | ROS와 LeRobot Python 환경 호환성 확인 |
| [adoodevv/so101_ros2](https://github.com/adoodevv/so101_ros2) **추천** | Jazzy용 URDF·MoveIt·Gazebo·실물 드라이버·리더 조작 | 기존 LeRobot 보정 사용; 원본 설정 절차 확인 |
| [phospho-app/phosphobot](https://github.com/phospho-app/phosphobot) | SO-101 조작·보정·데이터 기록·학습 UI/API | phospho MCP의 백엔드 |
| [moveit/moveit2](https://github.com/moveit/moveit2) | IK·충돌 검사·경로 계획 | ROS 2 조작 계획 기반 |
| [isaac-sim/IsaacLab](https://github.com/isaac-sim/IsaacLab) | 병렬 시뮬레이션과 강화학습 환경 | Isaac Sim 5.1에는 v2.3.x 계열 대응; main 버전 확인 |
| [NVIDIA/Isaac-GR00T](https://github.com/NVIDIA/Isaac-GR00T) | VLA 데이터 형식·미세조정·추론 | 사용 중인 N1.6과 최신 main의 차이 확인 |
| [NVlabs/curobo](https://github.com/NVlabs/curobo) | GPU 기반 IK·충돌 검사·궤적 최적화 | v1/v2 API 변경과 CUDA 의존성 확인 |
| [rail-berkeley/hil-serl](https://github.com/rail-berkeley/hil-serl) | 시연·사람 개입을 사용하는 실물 강화학습 | Franka 예제 중심; SO-101 환경 구현 필요 |
| [RobotWebTools/rosbridge_suite](https://github.com/RobotWebTools/rosbridge_suite) | ROS JSON·WebSocket 인터페이스 | ROS-MCP Server 등과 연결 |
| [modelcontextprotocol/python-sdk](https://github.com/modelcontextprotocol/python-sdk) | 자체 Python 코드를 MCP 도구로 노출 | 정책 학습 프레임워크와 별개의 인터페이스 |
| [NVlabs/ASPIRE](https://github.com/NVlabs/ASPIRE) | 로봇 작업용 코드와 재사용 동작 발견 연구 | 연구용; SO-101 연결은 별도 구현 |
| [dimensionalOS/dimos](https://github.com/dimensionalOS/dimos) | 로봇 인지·동작·에이전트 런타임과 MCP 연동 | 플랫폼 구조 참고; 로봇별 어댑터 확인 |

### 추가 모음집

| 원본 | 용도 | 연결 메모 |
|---|---|---|
| [chopinfeng/awesome-hardware-skills](https://github.com/chopinfeng/awesome-hardware-skills) | 하드웨어 MCP·에이전트 도구·시뮬레이터 모음 | 추가 프로젝트 탐색용 |
| [benchflow-ai/awesome-embodied-agents](https://github.com/benchflow-ai/awesome-embodied-agents) | 로봇 에이전트·모델·MCP·평가 자료 모음 | 추가 연구와 도구 탐색용 |

## 라이선스와 검토 범위

모음 코드와 문서는 MIT 라이선스입니다. 각 원본 프로젝트의 라이선스는 원본을 따릅니다. 출처 정보는 [THIRD_PARTY.md](THIRD_PARTY.md)와 [catalog.json](catalog.json)에 있습니다.

이 저장소에는 원본 프로젝트의 실행 코드를 복사해서 합치지 않았습니다. 소스 다운로드와 카탈로그 관리만 제공하며, 도구별 설치·실행과 로봇 어댑터는 각 프로젝트에서 진행합니다.

## 로컬 검증

```bash
python -m unittest discover -s tests -v
python hub.py list --recommended
python hub.py fetch --all --dry-run
```

