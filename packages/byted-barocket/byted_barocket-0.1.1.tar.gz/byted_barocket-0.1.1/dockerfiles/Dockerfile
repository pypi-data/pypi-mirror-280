# 从 pyo3/maturin 基础镜像开始
FROM ghcr.io/pyo3/maturin

# 安装 libssl-dev
RUN yum install -y openssl-devel

# 使用工作目录
WORKDIR /io

# 你可以在这里添加更多的设置或命令
# 例如，设置环境变量或运行预备脚本等