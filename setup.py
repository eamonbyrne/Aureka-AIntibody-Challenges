from setuptools import setup, find_packages

setup(
    name="aurabind",  # 改为你的包名（必须与 PyPI 上的名称一致）
    version="0.0.1",  # 版本号（遵循语义化版本：主版本.次版本.修订号）
    author="Aureka Inc",  # 替换为你的姓名/组织
    author_email="你的邮箱",  # 替换为你的邮箱
    description="你的包描述（如：A tool for protein binding analysis）",
    long_description=open("README.md").read(),  # 读取说明文档
    long_description_content_type="text/markdown",
    url="https://github.com/jxzly/Aureka-AIntibody-Challenges.git",  # 可选，如 https://github.com/你的账号/aurabind
    packages=find_packages(exclude=(
            "data",
            "esm_embeddings",
            "outputs",
            "release_data"
        )),  # 自动发现所有包（此时会找到 aurabind/）
    install_requires=[
        # 保留原包的依赖（如 numpy、torch 等，不要删除）
        "numpy>=1.21",
        "torch>=1.10",
        # ... 其他原依赖
    ],
    python_requires=">=3.11",  # 支持的 Python 版本
)