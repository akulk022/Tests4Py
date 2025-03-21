import os
from pathlib import Path
from typing import List, Optional, Tuple

from tests4py.constants import PYTHON
from tests4py.projects import Project, Status, TestingFramework, TestStatus
from tests4py.tests.generator import UnittestGenerator, SystemtestGenerator
from tests4py.tests.utils import API, TestResult

PROJECT_NAME = "keras"


class Keras(Project):
    def __init__(
        self,
        bug_id: int,
        buggy_commit_id: str,
        fixed_commit_id: str,
        test_files: List[Path],
        test_cases: List[str],
        test_status_fixed: TestStatus = TestStatus.PASSING,
        test_status_buggy: TestStatus = TestStatus.FAILING,
        unittests: Optional[UnittestGenerator] = None,
        systemtests: Optional[SystemtestGenerator] = None,
        api: Optional[API] = None,
        loc: int = 0,
        relevant_test_files: Optional[List[Path]] = None,
        skip_tests: Optional[List[str]] = None,
    ):
        super().__init__(
            bug_id=bug_id,
            project_name=PROJECT_NAME,
            github_url="https://github.com/keras-team/keras",
            status=Status.OK,
            python_version="3.7.8",
            python_path="",
            buggy_commit_id=buggy_commit_id,
            fixed_commit_id=fixed_commit_id,
            testing_framework=TestingFramework.PYTEST,
            test_files=test_files,
            test_cases=test_cases,
            test_status_fixed=test_status_fixed,
            test_status_buggy=test_status_buggy,
            unittests=unittests,
            systemtests=systemtests,
            api=api,
            grammar=None,
            loc=loc,
            included_files=[PROJECT_NAME],
            source_base=Path(PROJECT_NAME),
            test_base=Path("tests"),
            setup=[[PYTHON, "-m", "pip", "install", "-e", "."]],
            relevant_test_files=relevant_test_files,
            skip_tests=skip_tests,
        )

    def patch(self, location: Path):
        if self.bug_id in (14, 15, 16, 17, 18, 19, 20, 21, 22):
            with open(location / "setup.py", "r") as fp:
                content = fp.read()
            content = content.replace(
                "keras_applications==1.0.4",
                "keras_applications==1.0.6"
                if self.bug_id in (21, 22)
                else "keras_applications==1.0.8",
            )
            content = content.replace(
                "keras_preprocessing==1.0.2",
                "keras_preprocessing==1.0.5",
            )
            with open(location / "setup.py", "w") as fp:
                fp.write(content)
        if self.bug_id == 23:
            with open(location / "setup.py", "r") as fp:
                content = fp.read()
            content = content.replace(
                "keras_applications==1.0.2", "keras_applications==1.0.6"
            )
            content = content.replace(
                "keras_preprocessing==1.0.1",
                "keras_preprocessing==1.0.5",
            )
            with open(location / "setup.py", "w") as fp:
                fp.write(content)


def register():
    Keras(
        bug_id=1,
        buggy_commit_id="e32436144be933486182db6baee76c8746810488",
        fixed_commit_id="8e23a3ec47a2ccbf6cdd222a80886c6b9f17264f",
        test_files=[Path("tests", "keras", "initializers_test.py")],
        test_cases=[
            os.path.join(
                "tests", "keras", "initializers_test.py::test_statefulness[uniform]"
            ),
            os.path.join(
                "tests", "keras", "initializers_test.py::test_statefulness[orthogonal]"
            ),
            os.path.join(
                "tests",
                "keras",
                "initializers_test.py::test_statefulness[truncated_normal]",
            ),
            os.path.join(
                "tests", "keras", "initializers_test.py::test_statefulness[normal]"
            ),
            os.path.join(
                "tests",
                "keras",
                "initializers_test.py::test_statefulness[variance_scaling]",
            ),
        ],
        loc=22638,
    )
    Keras(
        bug_id=2,
        buggy_commit_id="65a215646c653ab808170c8b8c10de2945262613",
        fixed_commit_id="c24d16af155e20976bdf61e468ba760408e676ff",
        test_files=[Path("tests", "keras", "backend", "backend_test.py")],
        test_cases=[
            os.path.join(
                "tests",
                "keras",
                "backend",
                "backend_test.py::TestBackend::test_in_top_k",
            )
        ],
        skip_tests=[
            "test_gradient",
            "test_elementwise_operations",
            "(test_function and not test_function_tf)",
            "test_resize_images_bilinear",
        ],
        loc=22758,
    )
    Keras(
        bug_id=3,
        buggy_commit_id="e27b8b9343da4558b98570d6d45599bd0e365723",
        fixed_commit_id="c13d2723d01212d09dfdda39b0ad439803ec9230",
        test_files=[Path("tests", "keras", "test_sequential_model.py")],
        test_cases=[
            os.path.join(
                "tests",
                "keras",
                "test_sequential_model.py::test_clone_functional_model_with_multi_outputs",
            )
        ],
        loc=22751,
    )
    Keras(
        bug_id=4,
        buggy_commit_id="650c2c8cf9d711d35ab0ca7d1653ef53cbedaab3",
        fixed_commit_id="4185cbb50bfcae9cc30b0fc7b67e81d67a50a8ac",
        test_files=[Path("tests", "keras", "optimizers_test.py")],
        test_cases=[
            os.path.join(
                "tests",
                "keras",
                "optimizers_test.py::test_tfoptimizer_pass_correct_named_params_to_native_tensorflow_optimizer",
            )
        ],
        loc=22459,
    )
    Keras(
        bug_id=5,
        buggy_commit_id="1ebeff8ee304833a3df421d0de3b9f9480570eb9",
        fixed_commit_id="e11c48d9ce3ee47bb8a966549b14cbd5b10ee70d",
        test_files=[Path("tests", "keras", "utils", "data_utils_test.py")],
        test_cases=[
            os.path.join(
                "tests", "keras", "utils", "data_utils_test.py::test_data_utils"
            )
        ],
        loc=22261,
    )
    Keras(
        bug_id=6,
        buggy_commit_id="e32436144be933486182db6baee76c8746810488",
        fixed_commit_id="4b54657ab4806b0aaef8f8eeb973edb83c3d3483",
        test_files=[
            Path("tests", "test_loss_masking.py"),
            Path("tests", "test_loss_weighting.py"),
        ],
        test_cases=[
            os.path.join("tests", "test_loss_masking.py::test_masking_is_all_zeros")
        ],
        loc=22060,
    )
    Keras(
        bug_id=7,
        buggy_commit_id="be24159959672c32abb31697e721d96ae6ffaf97",
        fixed_commit_id="c05ef1fd95a6024155ab59656fef8dac5a45c335",
        test_files=[Path("tests", "keras", "wrappers", "scikit_learn_test.py")],
        test_cases=[
            os.path.join(
                "tests",
                "keras",
                "wrappers",
                "scikit_learn_test.py::test_regression_predict_shape_correct_num_test_1",
            )
        ],
        test_status_fixed=TestStatus.FAILING,
        loc=21990,
    )
    Keras(
        bug_id=8,
        buggy_commit_id="49f5b931410bc2e56378f20a15e8ac919e0efb88",
        fixed_commit_id="d78c982b326adeed6ac25200dc6892ff8f518ca6",
        test_files=[Path("tests", "keras", "engine", "test_topology.py")],
        test_cases=[
            os.path.join(
                "tests",
                "keras",
                "engine",
                "test_topology.py::test_layer_sharing_at_heterogeneous_depth_order",
            )
        ],
        skip_tests=[
            "test_recursion",
            "test_constant_initializer_with_numpy",
        ],
        loc=22427,
    )
    Keras(
        bug_id=9,
        buggy_commit_id="a07d9f3f3665ed79401f37f0c5759f271268a34f",
        fixed_commit_id="0505393746d56ddacc34bb1c016dba79429c9ac9",
        test_files=[
            Path("tests", "test_doc_auto_generation.py"),
        ],
        test_cases=[
            os.path.join(
                "tests", "test_doc_auto_generation.py::test_doc_lists[docs_descriptor1]"
            ),
        ],
        loc=22278,
    )
    Keras(
        bug_id=10,
        buggy_commit_id="58fd1f0589d33aeb33c4129cfedfb7737495efc0",
        fixed_commit_id="c1c4afe60b1355a6c0e83577791a0423f37a3324",
        test_files=[Path("tests", "keras", "engine", "test_training.py")],
        test_cases=[
            os.path.join(
                "tests", "keras", "engine", "test_training.py::test_sample_weights"
            )
        ],
        loc=22083,
    )
    Keras(
        bug_id=11,
        buggy_commit_id="58fd1f0589d33aeb33c4129cfedfb7737495efc0",
        fixed_commit_id="d6b5c5ebb410e3366c9d7aca41977a60134bfe10",
        test_files=[
            Path("tests", "integration_tests", "test_image_data_tasks.py"),
            Path("tests", "integration_tests", "test_temporal_data_tasks.py"),
        ],
        test_cases=[
            os.path.join(
                "tests",
                "integration_tests",
                "test_image_data_tasks.py::test_image_data_generator_training",
            ),
        ],
        loc=21230,
    )
    Keras(
        bug_id=12,
        buggy_commit_id="63c1757df519bc5756c0d7d79dabd5ec0420f3c8",
        fixed_commit_id="6dff721a3a8755356b2e89d02ef63ad8ab38ec95",
        test_files=[Path("tests", "keras", "metrics_test.py")],
        test_cases=[
            os.path.join(
                "tests",
                "keras",
                "metrics_test.py::test_sparse_categorical_accuracy_correctness[shape1]",
            ),
            os.path.join(
                "tests",
                "keras",
                "metrics_test.py::test_sparse_categorical_accuracy_correctness[shape2]",
            ),
        ],
        test_status_buggy=TestStatus.PASSING,
        loc=21126,
    )
    Keras(
        bug_id=13,
        buggy_commit_id="5027630fa41f499a9226a8f9d952ceabf2c247aa",
        fixed_commit_id="a07253d8269e1b750f0a64767cc9a07da8a3b7ea",
        test_files=[Path("tests", "keras", "engine", "test_training.py")],
        test_cases=[
            os.path.join(
                "tests", "keras", "engine", "test_training.py::test_model_methods"
            )
        ],
        loc=21127,
    )
    Keras(
        bug_id=14,
        buggy_commit_id="0bc8fac4463c68faa3b3c415c26eab02aa361fd5",
        fixed_commit_id="02bc5010a04bb11c8e91835cc9775c8149dec754",
        test_files=[Path("tests", "keras", "metrics_test.py")],
        test_cases=[
            os.path.join(
                "tests",
                "keras",
                "metrics_test.py::test_sparse_top_k_categorical_accuracy[y_pred1-y_true1]",
            )
        ],
        loc=21024,
    )
    Keras(
        bug_id=15,
        buggy_commit_id="4c01c0c4d77348416fff70e00ed6c25955c33ef6",
        fixed_commit_id="f60313e29657b2afb6a02f28dba5936bc0dd09e6",
        test_files=[Path("tests", "keras", "test_callbacks.py")],
        test_cases=[
            os.path.join("tests", "keras", "test_callbacks.py::test_CSVLogger")
        ],
        test_status_buggy=TestStatus.PASSING,
        loc=20893,
    )
    Keras(
        bug_id=16,
        buggy_commit_id="295bfe4e3ae7e98655b3630a9f83b2df4a82234f",
        fixed_commit_id="fe38f9dfc8c732a77ac03507b63c79b1d2acfba2",
        test_files=[Path("tests", "keras", "test_sequential_model.py")],
        test_cases=[
            os.path.join("tests", "keras", "test_sequential_model.py::test_sequential"),
            os.path.join(
                "tests",
                "keras",
                "test_sequential_model.py::test_sequential_deferred_build",
            ),
        ],
        loc=20910,
    )
    Keras(
        bug_id=17,
        buggy_commit_id="63c1757df519bc5756c0d7d79dabd5ec0420f3c8",
        fixed_commit_id="5a6af4bc6d44e9adbc2a21804bfcd18c4ce849ef",
        test_files=[Path("tests", "keras", "metrics_test.py")],
        test_cases=[
            os.path.join(
                "tests",
                "keras",
                "metrics_test.py::test_sparse_categorical_accuracy_correctness",
            )
        ],
        test_status_buggy=TestStatus.PASSING,
        loc=20691,
    )
    Keras(
        bug_id=18,
        buggy_commit_id="e74a37438b5389ae19eb61b431859f9789100874",
        fixed_commit_id="244546c2fe5165b6770eb456afd5fac8878473c5",
        test_files=[Path("tests", "keras", "backend", "backend_test.py")],
        test_cases=[
            os.path.join(
                "tests",
                "keras",
                "backend",
                "backend_test.py::TestBackend::test_function_tf_run_options_with_run_metadata",
            )
        ],
        skip_tests=[
            "test_gradient",
            "(test_function and not test_function_tf)",
            "test_in_top_k",
            "test_resize_images_bilinear",
            "test_spatial_2d_padding",
            "test_spatial_3d_padding",
            "test_batchnorm",
            "test_sparse_dot",
            "test_sparse_concat",
            "test_ctc_decode_beam_search",
        ],
        loc=20677,
    )
    Keras(
        bug_id=19,
        buggy_commit_id="295bfe4e3ae7e98655b3630a9f83b2df4a82234f",
        fixed_commit_id="66f8cc7ac4942f7f9fe0164a2a854a6264b87735",
        test_files=[Path("tests", "keras", "layers", "recurrent_test.py")],
        test_cases=[
            os.path.join(
                "tests",
                "keras",
                "layers",
                "recurrent_test.py::test_inconsistent_output_state_size",
            ),
            os.path.join(
                "tests",
                "keras",
                "layers",
                "recurrent_test.py::test_minimal_rnn_cell_non_layer_multiple_states",
            ),
            os.path.join(
                "tests",
                "keras",
                "layers",
                "recurrent_test.py::test_stacked_rnn_compute_output_shape",
            ),
        ],
        loc=20718,
    )
    Keras(
        bug_id=20,
        buggy_commit_id="ee8ff00a2a8a307c952fb8e7bef241188c7fb12b",
        fixed_commit_id="6dd087ab73b09e449144ff17450cc14f981b9ac2",
        test_files=[Path("tests", "keras", "layers", "convolutional_test.py")],
        test_cases=[
            os.path.join(
                "tests",
                "keras",
                "layers",
                "convolutional_test.py::test_conv2d_transpose_dilation",
            )
        ],
        loc=20699,
    )
    Keras(
        bug_id=21,
        buggy_commit_id="87417470c8168772559be0531e297120c569a422",
        fixed_commit_id="1fc585adb57f20a2acf69f0cd08b731259b8d2f8",
        test_files=[Path("tests", "keras", "test_callbacks.py")],
        test_cases=[
            os.path.join(
                "tests",
                "keras",
                "test_callbacks.py::test_EarlyStopping_final_weights_when_restoring_model_weights",
            )
        ],
        loc=20378,
    )
    Keras(
        bug_id=22,
        buggy_commit_id="54386efa549f850dff13f79fc3af67799a4e5d4f",
        fixed_commit_id="ee02d256611b17d11e37b86bd4f618d7f2a37d84",
        test_files=[Path("tests", "keras", "layers", "core_test.py")],
        test_cases=[
            os.path.join(
                "tests",
                "keras",
                "layers",
                "core_test.py::test_sequential_as_downstream_of_masking_layer",
            )
        ],
        loc=20447,
    )
    Keras(
        bug_id=23,
        buggy_commit_id="49f5b931410bc2e56378f20a15e8ac919e0efb88",
        fixed_commit_id="69c30a150f0b2caee7961ca1c0080960ef5ad6f6",
        test_files=[Path("tests", "keras", "test_sequential_model.py")],
        test_cases=[
            os.path.join(
                "tests",
                "keras",
                "test_sequential_model.py::test_nested_sequential_deferred_build",
            )
        ],
        loc=20647,
    )
    Keras(
        bug_id=24,
        buggy_commit_id="e34f9e6debf3b39da77c72e8a4c75cf7ccd94ef9",
        fixed_commit_id="bcf0031b54d555179be81c088cc3df0a723d7907",
        test_files=[Path("tests", "keras", "test_callbacks.py")],
        test_cases=[
            os.path.join(
                "tests",
                "keras",
                "test_callbacks.py::test_TensorBoard_multi_input_output",
            )
        ],
        loc=23663,
    )
    Keras(
        bug_id=25,
        buggy_commit_id="b470a595f7278acf5e7e47521edf25d3c4f479f1",
        fixed_commit_id="84e168b5fa55933e02e767ff7c86fcc0232aecc6",
        test_files=[
            Path("tests", "keras", "applications", "imagenet_utils_test.py"),
        ],
        test_cases=[
            os.path.join(
                "tests",
                "keras",
                "applications",
                "imagenet_utils_test.py::test_preprocess_input",
            )
        ],
        loc=23708,
    )
    Keras(
        bug_id=26,
        buggy_commit_id="08014eea360fd8d66b7baab19cdb9335f52c167b",
        fixed_commit_id="97d5fa920e4f8248128f7c1b460fd9bb20d3478f",
        test_files=[Path("tests", "keras", "backend", "backend_test.py")],
        test_cases=[
            os.path.join(
                "tests",
                "keras",
                "backend",
                "backend_test.py::TestBackend::test_rnn_additional_states",
            )
        ],
        skip_tests=[
            "test_linear_operations",
            "test_gradient",
            "(test_function and not test_function_tf)",
            "test_elementwise_operations",
            "test_nn_operations",
            "test_in_top_k",
            "test_ctc_decode_beam_search",
            "test_batchnorm",
            "test_sparse_dot",
            "test_sparse_concat",
            "test_arange",
            "test_in_test_phase",
            "test_in_train_phase",
        ],
        loc=23599,
    )
    Keras(
        bug_id=27,
        buggy_commit_id="49f5b931410bc2e56378f20a15e8ac919e0efb88",
        fixed_commit_id="b076e227da6beaf87d6c84eff1a92285e4662acf",
        test_files=[Path("tests", "keras", "layers", "wrappers_test.py")],
        test_cases=[
            os.path.join(
                "tests",
                "keras",
                "layers",
                "wrappers_test.py::test_Bidirectional_updates",
            ),
            os.path.join(
                "tests",
                "keras",
                "layers",
                "wrappers_test.py::test_Bidirectional_losses",
            ),
        ],
        loc=23414,
    )
    Keras(
        bug_id=28,
        buggy_commit_id="2e29ef31a7d61a84720a437801d2035b61d264fc",
        fixed_commit_id="5422fdd38baad36730cb6aeb946e17eeae6a551c",
        test_files=[Path("tests", "keras", "preprocessing", "sequence_test.py")],
        test_cases=[
            os.path.join(
                "tests",
                "keras",
                "preprocessing",
                "sequence_test.py::test_TimeSeriesGenerator_doesnt_miss_any_sample",
            ),
            os.path.join(
                "tests",
                "keras",
                "preprocessing",
                "sequence_test.py::test_TimeseriesGenerator",
            ),
        ],
        loc=23235,
    )
    Keras(
        bug_id=29,
        buggy_commit_id="e6c3f77b0b10b0d76778109a40d6d3282f1cadd0",
        fixed_commit_id="adc321b4d7a4e22f6bdb00b404dfe5e23d4887aa",
        test_files=[Path("tests", "keras", "metrics_test.py")],
        test_cases=[
            os.path.join(
                "tests", "keras", "metrics_test.py::test_stateful_metrics[dict]"
            )
        ],
        loc=23191,
    )
    Keras(
        bug_id=30,
        buggy_commit_id="4aa8aa100b00756c862c93ec4d0f8f44f091f48c",
        fixed_commit_id="2c8d1d03599cc03243bce8f07ed9c4a3d5f384f9",
        test_files=[Path("tests", "keras", "engine", "test_training.py")],
        test_cases=[
            os.path.join(
                "tests",
                "keras",
                "engine",
                "test_training.py::test_model_with_external_loss",
            )
        ],
        loc=23177,
    )
    Keras(
        bug_id=31,
        buggy_commit_id="e8190a8d8d4a59359f93bc9b366d04b9c72cc2ed",
        fixed_commit_id="e2a10a5e6e156a45e946c4d08db7133f997c1f9a",
        test_files=[Path("tests", "keras", "backend", "backend_test.py")],
        test_cases=[
            os.path.join(
                "tests", "keras", "backend", "backend_test.py::TestBackend::test_ctc"
            )
        ],
        skip_tests=[
            "test_linear_operations",
            "test_gradient",
            "(test_function and not test_function_tf)",
            "test_elementwise_operations",
            "test_nn_operations",
            "test_in_top_k",
            "test_batchnorm",
            "test_ctc_decode_beam_search",
            "test_sparse_dot",
            "test_sparse_concat",
            "test_arange",
            "test_in_train_phase",
        ],
        loc=23134,
    )
    Keras(
        bug_id=32,
        buggy_commit_id="4c01c0c4d77348416fff70e00ed6c25955c33ef6",
        fixed_commit_id="709f791af201caaab4aa180bda259989087cfe47",
        test_files=[Path("tests", "keras", "test_callbacks.py")],
        test_cases=[
            os.path.join(
                "tests", "keras", "test_callbacks.py::test_ReduceLROnPlateau_patience"
            ),
            os.path.join(
                "tests",
                "keras",
                "test_callbacks.py::test_ReduceLROnPlateau_backwards_compatibility",
            ),
        ],
        skip_tests=["tests_RemoteMonitor"],
        loc=23124,
    )
    Keras(
        bug_id=33,
        buggy_commit_id="37a1db225420851cc668600c49697d9a2057f098",
        fixed_commit_id="70ad0d6e4a569701ef106058397ad0540ec08340",
        test_files=[Path("tests", "keras", "preprocessing", "text_test.py")],
        test_cases=[
            os.path.join(
                "tests",
                "keras",
                "preprocessing",
                "text_test.py::test_text_to_word_sequence_multichar_split",
            ),
            os.path.join(
                "tests",
                "keras",
                "preprocessing",
                "text_test.py::test_text_to_word_sequence_unicode_multichar_split",
            ),
        ],
        loc=23085,
    )
    Keras(
        bug_id=34,
        buggy_commit_id="ab6b82c2dbcf5ede7d2950eca1efe815f5c0df75",
        fixed_commit_id="4b74fc5418944c9f449eb88ed4b40ada280fa5ca",
        test_files=[Path("tests", "test_multiprocessing.py")],
        test_cases=[
            os.path.join(
                "tests", "test_multiprocessing.py::test_multiprocessing_training"
            )
        ],
        loc=23036,
    )
    Keras(
        bug_id=35,
        buggy_commit_id="5430844453f5153f16dbd9d762d6a5a4106ba23f",
        fixed_commit_id="738819de0b7e6bc45abed8d0640f02b81c6ac4e9",
        test_files=[Path("tests", "keras", "preprocessing", "image_test.py")],
        test_cases=[
            os.path.join(
                "tests",
                "keras",
                "preprocessing",
                "image_test.py::TestImage::test_directory_iterator",
            )
        ],
        loc=22563,
    )
    Keras(
        bug_id=36,
        buggy_commit_id="c57bba20b0eb7bc1e70af6c71cc23a45de104b02",
        fixed_commit_id="fb1887d132a8ce8548ff53d868a6ba531cd63b34",
        test_files=[Path("tests", "keras", "layers", "convolutional_test.py")],
        test_cases=[
            os.path.join(
                "tests",
                "keras",
                "layers",
                "convolutional_test.py::test_separable_conv_1d",
            )
        ],
        loc=22278,
    )
    Keras(
        bug_id=37,
        buggy_commit_id="da21c15180d12a74a7c744c1f851a94c8b931a63",
        fixed_commit_id="1d2ad790dd43a2d702176c1170b2f3fd592a385a",
        test_files=[Path("tests", "keras", "layers", "wrappers_test.py")],
        test_cases=[
            os.path.join(
                "tests",
                "keras",
                "layers",
                "wrappers_test.py::test_Bidirectional_state_reuse",
            )
        ],
        loc=22237,
    )
    Keras(
        bug_id=38,
        buggy_commit_id="c506fbda4ac1d3df0f9a6111ba9bf75a20bc7b68",
        fixed_commit_id="64f80d6077edd5f277a1181df94bf4510ea0517a",
        test_files=[Path("tests", "keras", "layers", "recurrent_test.py")],
        test_cases=[
            os.path.join(
                "tests",
                "keras",
                "layers",
                "recurrent_test.py::test_minimal_rnn_cell_layer",
            )
        ],
        loc=22146,
    )
    Keras(
        bug_id=39,
        buggy_commit_id="2f266c3345ec65c721d4599a685fde6611fb8609",
        fixed_commit_id="a5ecde595c47f35fd7293d52eba48efd687ca94e",
        test_files=[Path("tests", "keras", "utils", "generic_utils_test.py")],
        test_cases=[
            os.path.join(
                "tests", "keras", "utils", "generic_utils_test.py::test_progbar"
            )
        ],
        loc=22117,
    )
    Keras(
        bug_id=40,
        buggy_commit_id="10d7e21efcf04bdb3438a809863a2fe728efe614",
        fixed_commit_id="4cad455ef4da600c96ddc69800bab39d0e52b677",
        test_files=[Path("tests", "keras", "layers", "recurrent_test.py")],
        test_cases=[
            os.path.join(
                "tests",
                "keras",
                "layers",
                "recurrent_test.py::test_stacked_rnn_compute_output_shape",
            )
        ],
        loc=21482,
    )
    Keras(
        bug_id=41,
        buggy_commit_id="5ae158e8b06562ab3db5d55d0f0a1dbda85d8089",
        fixed_commit_id="4a58b178073f0ba3b166220f7ebd7d56149bfb20",
        test_files=[Path("tests", "keras", "utils", "data_utils_test.py")],
        test_cases=[
            os.path.join(
                "tests",
                "keras",
                "utils",
                "data_utils_test.py::test_generator_enqueuer_fail_threads",
            ),
            os.path.join(
                "tests",
                "keras",
                "utils",
                "data_utils_test.py::test_generator_enqueuer_fail_processes",
            ),
        ],
        skip_tests=[
            "test_ordered_enqueuer_fail_threads",
            "test_ordered_enqueuer_fail_processes",
            "test_finite_generator_enqueuer_threads",
            "test_finite_generator_enqueuer_processes",
        ],
        loc=20988,
    )
    Keras(
        bug_id=42,
        buggy_commit_id="295bfe4e3ae7e98655b3630a9f83b2df4a82234f",
        fixed_commit_id="2f3edf96078d78450b985bdf3bfffe7e0c627169",
        test_files=[Path("tests", "keras", "engine", "test_training.py")],
        test_cases=[
            os.path.join(
                "tests", "keras", "engine", "test_training.py::test_model_methods"
            )
        ],
        loc=20868,
    )
    Keras(
        bug_id=43,
        buggy_commit_id="2264c13bf8e7242b9efb33ca8b5606e3c3a422ac",
        fixed_commit_id="b17169ca5d6cd1c8aeb237fc2bb0555c9e1b6a02",
        test_files=[
            Path("tests", "keras", "utils", "generic_utils_test.py"),
            Path("tests", "keras", "utils", "io_utils_test.py"),
            Path("tests", "keras", "utils", "layer_utils_test.py"),
            Path("tests", "keras", "utils", "multi_gpu_test.py"),
            Path("tests", "keras", "utils", "np_utils_test.py"),
            Path("tests", "keras", "utils", "vis_utils_test.py"),
        ],
        test_cases=[
            os.path.join(
                "tests", "keras", "utils", "np_utils_test.py::test_to_categorical"
            )
        ],
        loc=20859,
    )
    Keras(
        bug_id=44,
        buggy_commit_id="cc08f0f01fe97a9659e3da8fa9b290a54992c74a",
        fixed_commit_id="3292aa5a30350c67627f173ceac713956f68271f",
        test_files=[Path("tests", "keras", "layers", "recurrent_test.py")],
        test_cases=[
            os.path.join(
                "tests",
                "keras",
                "layers",
                "recurrent_test.py::test_trainability[SimpleRNN]",
            ),
            os.path.join(
                "tests", "keras", "layers", "recurrent_test.py::test_trainability[GRU]"
            ),
            os.path.join(
                "tests", "keras", "layers", "recurrent_test.py::test_trainability[LSTM]"
            ),
        ],
        loc=20825,
    )
    Keras(
        bug_id=45,
        buggy_commit_id="03a7eb89e27b70f2ca0ac932ef4bace7569d6fab",
        fixed_commit_id="159bb1aac17a8de0f96997d35703b8f26926a848",
        test_files=[Path("tests", "keras", "layers", "recurrent_test.py")],
        test_cases=[
            os.path.join(
                "tests",
                "keras",
                "layers",
                "recurrent_test.py::test_implementation_mode[LSTM]",
            )
        ],
        loc=20761,
    )


class KerasAPI(API):
    def __init__(self, default_timeout: int = 5):
        super().__init__(default_timeout=default_timeout)

    def oracle(self, args) -> Tuple[TestResult, str]:
        return TestResult.UNDEFINED, ""
