"""Test Dual UnitQuaternion related utility functions."""

from __future__ import annotations

import numpy as np
from dqrobotics import DQ, vec8
from spatialmath import UnitQuaternion

from screwmpcpy.dqutil import (
    delta_dq,
    dq_angle_norm,
    dq_exp,
    dq_log,
    dq_pose_error,
    dq_pow,
    dq_sclerp,
    dq_to_plucker,
    dq_to_pose,
    generate_intermediate_waypoints,
    interpolate_waypoints,
    plucker_to_dq,
    pose_to_dq,
)


def test_delta_dq() -> None:
    """
    Test delta DQ
    """
    initial_pose = (
        np.array([0, 1, 0]),
        UnitQuaternion(np.pi, np.array([1, 0, 0])),
    )
    goal_pose = (
        np.array([0, 0, -1]),
        UnitQuaternion(-np.pi / 4, np.array([0, 1, 0])),
    )

    initial_pose, goal_pose = pose_to_dq(initial_pose), pose_to_dq(goal_pose)
    delta = delta_dq(initial_pose, goal_pose)

    goal = initial_pose * delta
    assert goal == goal_pose


def test_pow() -> None:
    """Test pow for unit dual quaternions, which represent a screw motion."""

    pose = np.zeros((8,))
    pose[0] = 1.0
    pose[5:] = np.array([0.0, 0.0, -1.0])
    pose = DQ(pose)

    new_pose = dq_pow(pose, 0.5)
    np.testing.assert_array_equal(new_pose.D().vec3(), np.array([0.0, 0.0, -0.5]))


def test_exp_log() -> None:
    """Test exp and log unit dual quaternions."""
    pose = (
        np.array([0, 0, -1]),
        UnitQuaternion(-np.pi / 4, np.array([0, 1, 0])),
    )
    pose = pose_to_dq(pose)
    assert dq_exp(dq_log(pose)) == pose


def test_dq_angle_norm() -> None:
    """Test angle normalization of DQ stuff"""

    test_dq = DQ(np.zeros((8,)))
    assert test_dq == dq_angle_norm(test_dq)


def test_dq_sclerp() -> None:
    """Test scLERP for unit dual quaternions"""

    initial_pose = (
        np.array([0, 1, 0]),
        UnitQuaternion(np.pi, np.array([1, 0, 0])),
    )
    goal_pose = (
        np.array([0, 0, -1]),
        UnitQuaternion(-np.pi / 4, np.array([0, 1, 0])),
    )
    initial_pose, goal_pose = pose_to_dq(initial_pose), pose_to_dq(goal_pose)
    inter_pose = dq_sclerp(initial_pose, goal_pose, 0)
    assert inter_pose == initial_pose
    inter_pose = dq_sclerp(initial_pose, goal_pose, 1)
    assert inter_pose == goal_pose


def test_dq_plucker() -> None:
    """Test transformation to plucker screw"""

    # Check simple case (translation only)
    initial_pose = (
        np.array([1.0, 0.0, 0.0]),
        UnitQuaternion(np.pi, np.array([1, 0, 0])),
    )

    goal_pose = (np.array([0.0, 1.0, 0.0]), UnitQuaternion(np.pi, np.array([1, 0, 0])))
    expected_translation = goal_pose[0] - initial_pose[0]

    _initial_pose = pose_to_dq(initial_pose)
    _goal_pose = pose_to_dq(goal_pose)

    delta = _goal_pose * _initial_pose.inv()
    translation = delta.translation().vec3()
    axis, moment, angle, distance = dq_to_plucker(delta)
    _delta = plucker_to_dq(axis, moment, angle, distance)

    expected_axis = goal_pose[0] - initial_pose[0]
    expected_axis /= np.linalg.norm(expected_axis)

    assert np.isclose(distance, np.linalg.norm(expected_translation))
    assert np.isclose(angle, 0.0, atol=1e-6)
    assert delta == _delta

    np.testing.assert_almost_equal(expected_axis, axis)
    np.testing.assert_almost_equal(expected_translation, translation)

    # Check more rotation and translation
    initial_pose = (
        np.array([1.0, 0.0, 0.0]),
        UnitQuaternion(0.0, np.array([1, 0, 0])),
    )

    goal_pose = (
        np.array([0.0, 1.0, 0.0]),
        UnitQuaternion(np.pi / 2.0, np.array([0, 1, 0])),
    )

    _initial_pose = pose_to_dq(initial_pose)
    _goal_pose = pose_to_dq(goal_pose)

    delta = _goal_pose * _initial_pose.inv()
    axis, moment, angle, distance = dq_to_plucker(delta)
    _distance = np.dot(delta.translation().vec3(), delta.rotation_axis().vec3())
    _moment = 0.5 * (
        np.cross(delta.translation().vec3(), delta.rotation_axis().vec3())
        + (delta.translation().vec3() - _distance * delta.rotation_axis().vec3())
        / np.tan(delta.rotation_angle() / 2.0)
    )
    _delta = plucker_to_dq(axis, moment, angle, distance)

    assert _distance == distance
    assert angle == delta.rotation_angle()
    assert delta == _delta
    np.testing.assert_equal(_moment, moment)
    np.testing.assert_equal(axis, delta.rotation_axis().vec3())


def test_generate_waypoints() -> None:
    """Test the generated waypoints."""

    initial_pose = (
        np.array([0, 1, 0]),
        UnitQuaternion(np.pi, np.array([1, 0, 0])),
    )
    goal_pose = (
        np.array([0, 0, -1]),
        UnitQuaternion(-np.pi / 4, np.array([0, 1, 0])),
    )
    initial_pose, goal_pose = pose_to_dq(initial_pose), pose_to_dq(goal_pose)
    waypoints = generate_intermediate_waypoints(initial_pose, goal_pose, 10)

    assert len(waypoints) == 10

    steps = np.linspace(0, 1, len(waypoints))

    for step, waypoint in zip(steps, waypoints):
        inter_pose = dq_sclerp(initial_pose, goal_pose, step)
        assert inter_pose == waypoint


def test_dq_to_pose() -> None:
    """Test retrieved poses"""

    pose = (np.array([0, 1, 0]), UnitQuaternion(np.pi, np.array([1, 0, 0])))
    _pose = dq_to_pose(pose_to_dq(pose))
    np.testing.assert_array_almost_equal(pose[1].vec, _pose[1], decimal=12)
    np.testing.assert_array_almost_equal(pose[0], _pose[0], decimal=12)


def test_dq_pose_error() -> None:
    """Test retrieved pose error"""
    pose = (np.array([0, 1, 0]), UnitQuaternion(np.pi, np.array([1, 0, 0])))
    pose = pose_to_dq(pose)
    error = np.linalg.norm(dq_pose_error(pose, pose).vec8())
    assert error < 1e-15


def test_waypoints() -> None:
    """Test the generated intermediate way points."""

    initial_pose = (
        np.array([0, 1, 0]),
        UnitQuaternion(np.pi / 2, np.array([1, 0, 0])),
    )
    goal_pose = (
        np.array([0, 0, -1]),
        UnitQuaternion(-np.pi / 4, np.array([0, 1, 0])),
    )
    waypoints = interpolate_waypoints([initial_pose, goal_pose], 8)
    assert len(waypoints) == 10

    np.testing.assert_array_almost_equal(initial_pose[0], waypoints[0][0], decimal=12)
    np.testing.assert_array_almost_equal(
        initial_pose[1].vec, waypoints[0][1].vec, decimal=12
    )
    np.testing.assert_array_almost_equal(goal_pose[0], waypoints[-1][0], decimal=12)
    np.testing.assert_array_almost_equal(
        goal_pose[1].vec, waypoints[-1][1].vec, decimal=12
    )

    error = np.linalg.norm(
        vec8(dq_pose_error(pose_to_dq(initial_pose), pose_to_dq(goal_pose)))
    )
    expected_len = int((8 + 2) * np.clip(error, 0, 1))
    waypoints = interpolate_waypoints([initial_pose, goal_pose], 8, adaptive=True)
    assert len(waypoints) == expected_len
