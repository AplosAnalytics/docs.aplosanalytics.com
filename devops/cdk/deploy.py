#!/usr/bin/env python3
"""Aplos NCA SaaS UI — Deployment CLI (thin wrapper)."""
from pathlib import Path

from cdk_factory.commands.deployment_command import CdkDeploymentCommand

if __name__ == "__main__":
    CdkDeploymentCommand.main(script_dir=Path(__file__).parent)
