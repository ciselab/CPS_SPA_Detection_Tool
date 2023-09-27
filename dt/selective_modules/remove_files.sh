#!/bin/bash
set -e

dir_project=$1
keep_list=$2

if [[ "$dir_project" != '' ]] && [[ "$keep_list" != '' ]]; then

  dir_results=${HOME}/"results_px/"

  if [[ ! -d "$dir_results" ]]; then
    echo "Results directory does not yet exist..creating.."
    mkdir "$dir_results" &
    wait
  fi

  result_loc=${HOME}/"results_px/results_reverse.txt"
  if [[ -f "$result_loc" ]]; then
    echo "Results files already exist..removing.."
    rm -v "$result_loc" &
    wait
    echo "Results file has been removed."
  fi
  touch "$result_loc"

  echo "[RF] loc: $result_loc"
  echo "[RF] dir: $dir_project"
  echo "[RF] dir res: $dir_results"

  (cd "$dir_project" || exit; find -type f | grep -xv "$keep_list$(find -type f | grep -e "\./.git*")" > "$result_loc") &
#  (cd "$dir_project" || exit; find -type f | grep -xv "./src/modules/mavlink/mavlink_main.cpp\|./src/modules/commander/commander.cpp\|./src/drivers/gps/gps.cpp\|./platforms/common/include/px4_platform_common/px4_work_queue/WorkQueueManager.hpp\|./src/modules/navigator/navigator_main.cpp\|./src/modules/sdlog2/sdlog2.c\|./src/modules/mc_pos_control/mc_pos_control_params.c\|./src/modules/fw_att_control/fw_att_control_main.cpp\|./src/modules/logger/logger.cpp\|./src/drivers/px4fmu/fmu.cpp\|./src/modules/mc_att_control/mc_att_control_params.c\|./src/modules/sensors/sensors.cpp\|./src/modules/mavlink/mavlink_receiver.cpp\|./src/drivers/frsky_telemetry/frsky_telemetry.c\|./src/modules/ekf_att_pos_estimator/ekf_att_pos_estimator_main.cpp\|./src/modules/logger/logged_topics.cpp\|./src/modules/fw_pos_control_l1/fw_pos_control_l1_main.cpp\|./src/modules/attitude_estimator_q/attitude_estimator_q_main.cpp\|./src/modules/mavlink/mavlink.c\|./src/modules/commander/Commander.cpp\|./src/modules/commander/commander_params.c\|./src/modules/mc_att_control/mc_att_control_main.cpp\|./src/drivers/px4io/px4io.cpp\|./src/modules/mc_pos_control/mc_pos_control_main.cpp\|./src/modules/ekf2/ekf2_main.cpp\|./src/modules/commander/calibration_routines.cpp\|./apps/px4io/px4io.c\|./src/modules/commander/PreflightCheck.cpp\|./src/modules/sensors/sensor_params.c\|./src/platforms/common/px4_work_queue/WorkQueueManager.hpp\|./src/modules/commander/esc_calibration.cpp\|./src/modules/logger/log_writer_file.cpp\|./src/modules/mavlink/mavlink_mission.cpp\|./src/modules/fw_att_control/fw_att_control_params.c\|./src/modules/position_estimator_inav/position_estimator_inav_main.c\|./src/drivers/tap_esc/tap_esc.cpp\|./src/drivers/pmw3901/pmw3901.cpp\|./src/drivers/ms5611/ms5611_spi.cpp\|./src/modules/vtol_att_control/vtol_att_control_main.cpp\|./src/drivers/mpu6000/mpu6000.cpp\|./src/drivers/telemetry/iridiumsbd/IridiumSBD.cpp\|./src/lib/controllib/block/Block.hpp\|./src/modules/uORB/uORB_tests/uORBTest_UnitTest.hpp\|./apps/mavlink/mavlink.c\|./src/modules/fw_pos_control_l1/FixedwingPositionControl.cpp\|./src/drivers/frsky_telemetry/sPort_data.c\|./src/modules/mavlink/mavlink_messages.cpp\|./src/modules/position_estimator_inav/position_estimator_inav_main.cpp\|./apps/px4io/controls.c\|./apps/px4io/px4io.h\|./src/modules/sensors/voted_sensors_update.cpp\|./src/modules/commander/state_machine_helper.cpp\|./src/modules/land_detector/LandDetector.h\|./src/modules/land_detector/land_detector_params_fw.c\|./src/drivers/imu/mpu9250/mpu9250.cpp\|./src/drivers/imu/mpu9250/mpu9250.h\|./src/drivers/distance_sensor/ll40ls/LidarLiteI2C.cpp\|./src/drivers/telemetry/frsky_telemetry/frsky_telemetry.cpp\|./src/drivers/boards/crazyflie/board_config.h\|./src/systemcmds/nshterm/nshterm.c\|./src/modules/ekf2/ekf2_params.c\|./src/modules/simulator/simulator_mavlink.cpp\|./src/drivers/vmount/vmount.cpp\|./src/platforms/px4_tasks.h\|./src/modules/mavlink/orb_listener.c\|./src/drivers/magnetometer/lis2mdl/lis2mdl.h\|./src/modules/navigator/rtl_params.c\|./src/modules/bottle_drop/bottle_drop.cpp\|./apps/mavlink/mavlink_receiver.c\|./src/modules/mavlink/mavlink_mission.h\|./src/drivers/spektrum_rc/spektrum_rc.cpp\|./src/drivers/px4io/interface_serial.cpp\|./src/lib/launchdetection/CatapultLaunchMethod.cpp\|./src/lib/launchdetection/CatapultLaunchMethod.h\|./src/lib/launchdetection/LaunchDetector.cpp\|./src/lib/launchdetection/LaunchDetector.h\|./src/lib/launchdetection/LaunchMethod.h\|./src/modules/navigator/geofence.cpp\|./src/modules/navigator/geofence.h\|./src/modules/commander/PreflightCheck.h\|./src/modules/mavlink/mavlink_orb_subscription.cpp\|./src/drivers/sPort_telemetry/sPort_data.c\|./src/drivers/sPort_telemetry/sPort_telemetry.c\|./src/drivers/boards/px4fmu-v4/px4fmu_init.c\|./src/drivers/distance_sensor/airlango/isl2950.cpp\|./src/drivers/distance_sensor/airlango/isl2950_parser.cpp\|./src/drivers/distance_sensor/airlango/isl2950_parser.h\|./src/modules/commander/mag_calibration.cpp\|./src/modules/navigator/mission_block.cpp\|./src/modules/navigator/mission_block.h\|./src/modules/navigator/mission_params.c\|./src/modules/mc_pos_control/PositionControl.cpp\|./EKF/terrain_estimator.cpp\|./src/lib/CollisionPrevention/CollisionPrevention.cpp\|./src/lib/CollisionPrevention/CollisionPrevention.hpp\|./src/lib/CollisionPrevention/CollisionPreventionTest.cpp\|./src/lib/CollisionPrevention/collisionprevention_params.c\|./src/platforms/posix/main.cpp\|./apps/sensors/sensors.cpp\|./src/drivers/frsky_telemetry/frsky_data.c\|./src/drivers/hott/messages.cpp\|./src/examples/px4_simple_app/px4_simple_app.c\|./src/lib/terrain_estimation/terrain_estimator.cpp\|./src/modules/attitude_estimator_ekf/attitude_estimator_ekf_main.cpp\|./src/modules/ekf2_replay/ekf2_replay_main.cpp\|./src/modules/ekf_att_pos_estimator/AttitudePositionEstimatorEKF.h\|./src/modules/local_position_estimator/BlockLocalPositionEstimator.cpp\|./src/modules/local_position_estimator/sensors/baro.cpp\|./src/platforms/common/shutdown.cpp\|./apps/px4io/registers.c\|./src/drivers/imu/adis16477/ADIS16477.cpp\|./boards/px4/fmu-v5x/src/board_config.h\|./src/drivers/imu/invensense/mpu6000/InvenSense_MPU6000_registers.hpp\|./src/drivers/imu/invensense/mpu6000/MPU6000.cpp\|./src/drivers/imu/invensense/mpu6000/MPU6000.hpp\|./src/modules/land_detector/FixedwingLandDetector.cpp\|./src/modules/land_detector/FixedwingLandDetector.h\|./src/modules/land_detector/land_detector_params.c\|./src/modules/land_detector/land_detector_params_mc.c\|./src/lib/drivers/device/integrator.h\|./platforms/common/include/px4_platform_common/module.h\|./apps/sdlog/sdlog.c\|./src/drivers/mpu9250/mpu9250_spi.cpp\|./src/drivers/distance_sensor/tfmini/TFMINI.cpp\|./src/modules/navigator/mission.cpp\|./src/modules/vtol_att_control/standard.cpp\|./src/modules/vtol_att_control/vtol_att_control_params.c\|./src/modules/systemlib/system_params.c\|./src/lib/sensor_calibration/Accelerometer.cpp\|./src/lib/sensor_calibration/Gyroscope.cpp\|./src/lib/sensor_calibration/Magnetometer.cpp\|./src/modules/position_estimator_inav/position_estimator_inav_params.c\|./src/modules/position_estimator_inav/position_estimator_inav_params.h\|./src/modules/uORB/topics/vehicle_local_position.h\|./src/modules/mavlink/mavlink_log_handler.cpp\|./src/modules/uORB/uORB_tests/uORBTest_UnitTest.cpp\|./nuttx/drivers/mtd/sst25.c\|./src/modules/mavlink/mavlink_main.h\|./src/drivers/gimbal/gimbal.cpp\|./src/modules/commander/state_machine_helper.h\|./test/sensor_simulator/sensor_simulator.cpp\|./apps/drivers/ms5611/ms5611.cpp\|./apps/fixedwing_control/fixedwing_control.c\|./apps/fixedwing_control/fixedwing_control.h\|./apps/fixedwing_control/pid.c\|./apps/px4/attitude_estimator_bm/attitude_estimator_bm.c\|./apps/px4/px4io/driver/px4io.cpp\|./apps/sensors/sensors.c\|./nuttx/configs/px4fmu/include/nsh_romfsimg.h\|./nuttx/configs/px4fmu/src/drv_hmc5833l.c\|./nuttx/configs/px4fmu/src/drv_ms5611.c\|./src/platforms/posix/drivers/gyrosim/gyrosim.cpp\|./src/lib/FlightTasks/tasks/Auto/FlightTaskAuto.cpp\|./src/lib/FlightTasks/tasks/Manual/FlightTaskManual.cpp\|./src/lib/FlightTasks/tasks/Manual/FlightTaskManual.hpp\|./src/modules/vtol_att_control/tailsitter.cpp\|./src/modules/ekf2/Utility/PreFlightChecker.cpp\|./src/modules/ekf2/Utility/PreFlightChecker.hpp\|./src/modules/syslink/syslink_bridge.cpp\|./src/modules/syslink/syslink_main.cpp\|./src/modules/syslink/syslink_main.h\|./src/modules/commander/gyro_calibration.cpp\|./src/modules/mavlink/mavlink_receiver.h\|./src/modules/load_mon/load_mon.cpp\|./src/modules/uavcan/uavcan_main.hpp\|./src/drivers/imu/bmi055/BMI055_accel.cpp\|./src/drivers/distance_sensor/ll40ls/LidarLiteI2C.h\|./src/drivers/device/vdev_posix.cpp\|./src/drivers/distance_sensor/vl53lxx/vl53lxx.cpp\|./src/drivers/bmi160/bmi160.cpp\|./src/drivers/protocol_splitter/protocol_splitter.cpp\|./apps/drivers/px4io/uploader.cpp\|./src/modules/sdlog2/sdlog2_messages.h\|./src/lib/led/led.cpp\|./src/lib/led/led.h\|./src/modules/multirotor_pos_control/multirotor_pos_control.c\|./src/drivers/ms5611/ms5611_nuttx.cpp\|./src/drivers/camera_trigger/camera_trigger.cpp\|./src/drivers/px4io/px4io_i2c.cpp\|./apps/px4io/comms.c\|./apps/px4io/mixer.c\|./src/modules/sensors/parameters.cpp\|./src/modules/sensors/rc_update.cpp\|./src/drivers/hott/hott_sensors/hott_sensors.cpp\|./src/drivers/pwm_out_sim/pwm_out_sim.cpp\|./src/modules/local_position_estimator/sensors/flow.cpp\|./src/drivers/ist8310/ist8310.cpp\|./platforms/posix/src/lockstep_scheduler/include/lockstep_scheduler/lockstep_scheduler.h\|./platforms/posix/src/lockstep_scheduler/src/lockstep_scheduler.cpp\|./platforms/posix/src/lockstep_scheduler/test/src/lockstep_scheduler_test.cpp\|./src/modules/px4iofirmware/registers.c\|./src/modules/logger/messages.h\|./src/drivers/stm32/drv_hrt.c\|./src/modules/systemlib/perf_counter.c\|./src/modules/systemlib/perf_counter.h\|./src/systemcmds/perf/perf.c\|./src/drivers/distance_sensor/broadcom/afbrs50/AFBRS50.cpp\|./src/drivers/distance_sensor/broadcom/afbrs50/AFBRS50.hpp\|./src/drivers/distance_sensor/broadcom/afbrs50/API/Src/timer.c\|./src/drivers/distance_sensor/broadcom/afbrs50/argus_hal_test.c\|./src/drivers/distance_sensor/broadcom/afbrs50/argus_hal_test.h\|./src/modules/px4iofirmware/adc.c\|./src/modules/fw_pos_control_l1/fw_pos_control_l1_params.c\|./src/modules/dataman/dataman.h\|./src/modules/navigator/navigation.h\|./src/modules/muorb/adsp/px4muorb.cpp\|./src/modules/uORB/uORBDevices.cpp\|./src/systemcmds/mixer/mixer.c\|./src/platforms/posix/drivers/accelsim/accelsim.cpp\|./src/modules/commander/Commander.hpp\|./src/systemcmds/tests/test_hrt.c\|./src/drivers/pwm_out_sim/PWMSim.cpp\|./src/drivers/stm32/drv_io_timer.c\|./src/drivers/l3gd20/l3gd20.cpp\|./src/drivers/boards/tap-v1/board_config.h\|./src/drivers/boards/tap-v1/tap_pwr.c\|./src/modules/local_position_estimator/local_position_estimator_main.cpp\|./src/platforms/px4_posix.h\|./src/modules/fw_att_pos_estimator/estimator.cpp\|./src/modules/fw_att_pos_estimator/estimator.h\|./src/modules/fw_att_pos_estimator/fw_att_pos_estimator_main.cpp\|./src/modules/commander/esc_calibration.h\|./EKF/estimator_interface.cpp\|./src/modules/logger/logger.h\|./.git/HEAD\|./.git/hooks/pre-commit.sample\|./.git/hooks/prepare-commit-msg.sample\|./.git/hooks/pre-merge-commit.sample\|./.git/hooks/pre-push.sample\|./.git/hooks/update.sample\|./.git/hooks/commit-msg.sample\|./.git/hooks/pre-receive.sample\|./.git/hooks/post-update.sample\|./.git/hooks/pre-rebase.sample\|./.git/hooks/pre-applypatch.sample\|./.git/hooks/fsmonitor-watchman.sample\|./.git/hooks/applypatch-msg.sample\|./.git/logs/HEAD\|./.git/logs/refs/heads/main\|./.git/logs/refs/remotes/origin/HEAD\|./.git/config\|./.git/objects/pack/pack-a1ceceab882690ada83718c90f120d0db52aed7b.idx\|./.git/objects/pack/pack-a1ceceab882690ada83718c90f120d0db52aed7b.pack\|./.git/info/exclude\|./.git/packed-refs\|./.git/index\|./.git/refs/remotes/origin/HEAD\|./.git/refs/heads/main\|./.git/description\|./.github/stale.yml\|./.github/ISSUE_TEMPLATE/1_Bug_report.md\|./.github/ISSUE_TEMPLATE/2_Feature_request.md\|./.github/ISSUE_TEMPLATE/3_Support_question.md\|./.github/ISSUE_TEMPLATE/4_Documentation_issue.md\|./.github/slack.svg\|./.github/workflows/compile_nuttx_cannode.yml\|./.github/workflows/mavros_mission_tests.yml\|./.github/workflows/ekf_update_change_indicator.yml\|./.github/workflows/metadata.yml\|./.github/workflows/clang-tidy.yml\|./.github/workflows/compile_nuttx.yml\|./.github/workflows/compile_linux_arm64.yml\|./.github/workflows/python_checks.yml\|./.github/workflows/compile_macos.yml\|./.github/workflows/deploy_all.yml\|./.github/workflows/compile_linux.yml\|./.github/workflows/ekf_functional_change_indicator.yml\|./.github/workflows/mavros_offboard_tests.yml\|./.github/workflows/checks.yml\|./.github/workflows/sitl_tests.yml\|./.gitmodules\|./.git/objects/pack/pack-3bacaf8ab2bfe6609756e2f2046a827a7bd2f684.idx\|./.git/objects/pack/pack-3bacaf8ab2bfe6609756e2f2046a827a7bd2f684.pack\|./.gitattributes\|./.github_changelog_generator\|$(find -type f | grep -e "\./.git*")" > "$result_loc") &
  wait

  if [[ "$result_loc" =~ \./git ]]; then
    echo "[RF] ERROR: .git* file still found."
  else
    echo "Removing files..."
    while read -r line
    do
      (cd "$dir_project" || exit; rm "$line") &
      wait
    done < "$result_loc"
  fi
  wait
else
  echo "Empty directory input, stopping."
fi
