"""Collection of tests for unified neural network activation functions."""

# global
import numpy as np
from hypothesis import given, strategies as st

# local
import ivy_tests.test_ivy.helpers as helpers
import ivy.functional.backends.numpy as ivy_np


# relu
@given(
    dtype_and_x=helpers.dtype_and_values(available_dtypes=ivy_np.valid_float_dtypes),
    as_variable=st.booleans(),
    with_out=st.booleans(),
    num_positional_args=helpers.num_positional_args(fn_name="relu"),
    container=st.booleans(),
    instance_method=st.booleans(),
    native_array=st.booleans(),
)
def test_relu(
    dtype_and_x,
    as_variable,
    with_out,
    num_positional_args,
    container,
    instance_method,
    native_array,
    fw,
):
    dtype, x = dtype_and_x
    helpers.test_function(
        input_dtypes=dtype,
        as_variable_flags=as_variable,
        with_out=with_out,
        native_array_flags=native_array,
        fw=fw,
        num_positional_args=num_positional_args,
        container_flags=container,
        instance_method=instance_method,
        fn_name="relu",
        x=np.asarray(x, dtype=dtype),
    )


# leaky_relu
@given(
    dtype_and_x=helpers.dtype_and_values(available_dtypes=ivy_np.valid_float_dtypes),
    as_variable=st.booleans(),
    with_out=st.booleans(),
    native_array=st.booleans(),
    num_positional_args=helpers.num_positional_args(fn_name="leaky_relu"),
    container=st.booleans(),
    instance_method=st.booleans(),
    alpha=st.floats(width=16),
)
def test_leaky_relu(
    dtype_and_x,
    alpha,
    as_variable,
    with_out,
    num_positional_args,
    container,
    instance_method,
    native_array,
    fw,
):
    dtype, x = dtype_and_x
    helpers.test_function(
        input_dtypes=dtype,
        as_variable_flags=as_variable,
        with_out=with_out,
        native_array_flags=native_array,
        fw=fw,
        num_positional_args=num_positional_args,
        container_flags=container,
        instance_method=instance_method,
        fn_name="leaky_relu",
        test_rtol=1e-4,
        x=np.asarray(x, dtype=dtype),
        alpha=alpha,
    )


# gelu
@given(
    dtype_and_x=helpers.dtype_and_values(available_dtypes=ivy_np.valid_float_dtypes),
    as_variable=st.booleans(),
    with_out=st.booleans(),
    approximate=st.booleans(),
    num_positional_args=helpers.num_positional_args(fn_name="gelu"),
    container=st.booleans(),
    instance_method=st.booleans(),
    native_array=st.booleans(),
)
def test_gelu(
    dtype_and_x,
    as_variable,
    with_out,
    approximate,
    num_positional_args,
    container,
    instance_method,
    native_array,
    fw,
):
    dtype, x = dtype_and_x
    helpers.test_function(
        input_dtypes=dtype,
        as_variable_flags=as_variable,
        with_out=with_out,
        native_array_flags=native_array,
        fw=fw,
        num_positional_args=num_positional_args,
        container_flags=container,
        instance_method=instance_method,
        fn_name="gelu",
        test_atol=1e-4,
        test_rtol=1e-4,
        x=np.asarray(x, dtype=dtype),
        approximate=approximate,
    )


# tanh
@given(
    dtype_and_x=helpers.dtype_and_values(available_dtypes=ivy_np.valid_float_dtypes),
    as_variable=st.booleans(),
    with_out=st.booleans(),
    num_positional_args=helpers.num_positional_args(fn_name="tanh"),
    container=st.booleans(),
    instance_method=st.booleans(),
    native_array=st.booleans(),
)
def test_tanh(
    dtype_and_x,
    as_variable,
    with_out,
    num_positional_args,
    container,
    instance_method,
    native_array,
    fw,
):
    dtype, x = dtype_and_x
    helpers.test_function(
        input_dtypes=dtype,
        as_variable_flags=as_variable,
        with_out=with_out,
        native_array_flags=native_array,
        fw=fw,
        num_positional_args=num_positional_args,
        container_flags=container,
        instance_method=instance_method,
        fn_name="tanh",
        x=np.asarray(x, dtype=dtype),
    )


# sigmoid
@given(
    dtype_and_x=helpers.dtype_and_values(available_dtypes=ivy_np.valid_float_dtypes),
    as_variable=st.booleans(),
    with_out=st.booleans(),
    num_positional_args=helpers.num_positional_args(fn_name="sigmoid"),
    container=st.booleans(),
    instance_method=st.booleans(),
    native_array=st.booleans(),
)
def test_sigmoid(
    dtype_and_x,
    as_variable,
    with_out,
    num_positional_args,
    container,
    instance_method,
    native_array,
    fw,
):
    dtype, x = dtype_and_x
    helpers.test_function(
        input_dtypes=dtype,
        as_variable_flags=as_variable,
        with_out=with_out,
        native_array_flags=native_array,
        fw=fw,
        num_positional_args=num_positional_args,
        container_flags=container,
        instance_method=instance_method,
        fn_name="sigmoid",
        x=np.asarray(x, dtype=dtype),
    )


# softmax
@given(
    dtype_and_x=helpers.dtype_and_values(
        available_dtypes=ivy_np.valid_float_dtypes, min_num_dims=1
    ),
    as_variable=st.booleans(),
    with_out=st.booleans(),
    axis=st.integers(-1, 0),
    num_positional_args=helpers.num_positional_args(fn_name="softmax"),
    container=st.booleans(),
    instance_method=st.booleans(),
    native_array=st.booleans(),
)
def test_softmax(
    dtype_and_x,
    as_variable,
    axis,
    with_out,
    num_positional_args,
    container,
    instance_method,
    native_array,
    fw,
):
    dtype, x = dtype_and_x
    helpers.test_function(
        input_dtypes=dtype,
        as_variable_flags=as_variable,
        with_out=with_out,
        native_array_flags=native_array,
        fw=fw,
        num_positional_args=num_positional_args,
        container_flags=container,
        instance_method=instance_method,
        fn_name="softmax",
        x=np.asarray(x, dtype=dtype),
        axis=axis,
    )


# softplus
@given(
    dtype_and_x=helpers.dtype_and_values(
        available_dtypes=ivy_np.valid_float_dtypes, min_num_dims=1
    ),
    as_variable=st.booleans(),
    with_out=st.booleans(),
    num_positional_args=helpers.num_positional_args(fn_name="softplus"),
    container=st.booleans(),
    instance_method=st.booleans(),
    native_array=st.booleans(),
)
def test_softplus(
    dtype_and_x,
    as_variable,
    with_out,
    num_positional_args,
    container,
    instance_method,
    native_array,
    fw,
):
    dtype, x = dtype_and_x
    helpers.test_function(
        input_dtypes=dtype,
        as_variable_flags=as_variable,
        with_out=with_out,
        native_array_flags=native_array,
        fw=fw,
        num_positional_args=num_positional_args,
        container_flags=container,
        instance_method=instance_method,
        fn_name="softplus",
        x=np.asarray(x, dtype=dtype),
    )
