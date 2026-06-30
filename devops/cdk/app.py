"""
Aplos NCA Documentation Site — Infrastructure as Code
Maintainers: Aplos NCA Team
MIT License. See Project Root for the license information.
"""

import os
from pathlib import Path

from cdk_factory.app import CdkAppFactory


class AplosDocsIaC:
    """Aplos NCA Documentation Infrastructure"""

    def __init__(self):
        self.name = "AplosDocsIaC"

    def synth(self):
        """Synth the docs infrastructure"""
        print("synth", self.name)
        path = str(Path(__file__).parent)
        project_path = str(Path(__file__).parent.parent)
        config_path = os.path.join(path, "config.json")
        if not os.path.exists(config_path):
            raise FileNotFoundError(f"Config file not found: {config_path}")

        # cdk.out lives alongside app.py in the cdk/ directory
        outdir = "./cdk.out"
        # the CdkAppFactory will use some "canned" or pre-made stacks
        factory: CdkAppFactory = CdkAppFactory(
            config_path="./config.json", runtime_directory=path, outdir=outdir
        )

        # this assumes your cdk file (app.py) will be at the root of your project
        cdk_app_file = "./app.py"

        full_path = os.path.join(path, cdk_app_file)
        if not os.path.exists(full_path):
            message: str = (
                "Warning, we could not locate your app.py, which is the "
                "entry point to your cdk deployment. "
                f"Expected to find it here: {full_path}"
            )
            raise FileNotFoundError(message)

        cloud_assembly = factory.synth(
            paths=[path, project_path], cdk_app_file=cdk_app_file
        )

        return cloud_assembly


def main():
    """Run the app"""
    app = AplosDocsIaC()
    app.synth()


if __name__ == "__main__":
    main()
