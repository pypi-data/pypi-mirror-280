load(
    "@rules_foreign_cc//foreign_cc:defs.bzl", "cmake", "configure_make", "make"
)

load("@pybind11_bazel//:build_defs.bzl", "pybind_extension")

cc_binary(
    name="simple_test",
    srcs=["simple_test.cc"],
)

cc_library(
    name="create_database",
    srcs=["create_database.cc", "pdqsort.h"],
    hdrs=["create_database.hh"],
    deps=[
        ":arrow", 
        "@com_google_absl//absl/types:optional",
        "@com_google_absl//absl/container:flat_hash_map",
        "@readerwriterqueue",
        "@concurrentqueue",
        ":zstd",
        ":streamvbyte",
    ],
)

cc_binary(
    name="main",
    srcs=["main.cc"],
    deps=[
        ":create_database", 
    ],
)


pybind_extension(
    name="_meds_reader",
    srcs=[
        "meds_reader.cc",
    ],
    deps=[":create_database"],
)

cmake(
    name = "arrow",
    build_args = [
        "-j `nproc`",
    ],
    cache_entries = {
        "CMAKE_C_FLAGS": "-fPIC -I/usr/include",
        "CMAKE_CXX_FLAGS": "-fPIC -I/usr/include",
        "ARROW_BUILD_SHARED": "OFF",
        "ARROW_BUILD_STATIC": "ON",
        "ARROW_BUILD_TESTS": "OFF",
        "ARROW_PARQUET": "ON",
        "ARROW_WITH_SNAPPY": "ON",
        "ARROW_WITH_ZSTD": "ON",
        "EP_COMMON_CMAKE_ARGS": "-DWITH_OPENSSL=OFF",
        "ARROW_DEPENDENCY_SOURCE": "BUNDLED",
        "CMAKE_INSTALL_LIBDIR": "lib",
    },
    tags = ["requires-network"],
    generate_args = ["-DCMAKE_RANLIB=/usr/bin/ranlib"],
    working_directory="cpp",
    lib_source = "@arrow//:all",
    # out_lib_dir = "lib64",
    out_static_libs = ["libparquet.a", "libarrow.a", "libarrow_bundled_dependencies.a"],
    linkopts = ["-pthread"],
)

cmake(
    name = "zstd",
    cache_entries = {
        "CMAKE_C_FLAGS": "-fPIC",
        "CMAKE_CXX_FLAGS": "-fPIC",
        "CMAKE_INSTALL_LIBDIR": "lib",
    },
    working_directory="build/cmake",
    lib_source = "@zstd//:all",
    # out_lib_dir = "lib64",
    out_static_libs = ["libzstd.a"],
)

cmake(
    name = "streamvbyte",
    cache_entries = {
        "CMAKE_C_FLAGS": "-fPIC",
        "CMAKE_CXX_FLAGS": "-fPIC",
    },
    lib_source = "@streamvbyte//:all",
    # out_lib_dir = "lib64",
    out_static_libs = ["libstreamvbyte.a"],
)