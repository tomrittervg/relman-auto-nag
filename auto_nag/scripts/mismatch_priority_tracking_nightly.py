# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.

from auto_nag.bzcleaner import BzCleaner


class MismatchPrioTrackNightly(BzCleaner):
    def __init__(self):
        super(MismatchPrioTrackNightly, self).__init__()
        self.init_versions()

    def description(self):
        return "Bug tracked for nightly with a bad priority (P3, P4 or P5)"

    def template(self):
        return "mismatch_priority_tracking.html"

    def ignore_date(self):
        return True

    def get_bz_params(self, date):
        central_version = self.versions["central"]
        value = ",".join(["---", "affected"])
        params = {
            "resolution": [
                "---",
                "FIXED",
                "INVALID",
                "WONTFIX",
                "DUPLICATE",
                "WORKSFORME",
                "INCOMPLETE",
                "SUPPORT",
                "EXPIRED",
                "MOVED",
            ],
            "priority": ["P3", "P4", "P5"],
            "f1": "cf_tracking_firefox" + central_version,
            "o1": "anyexact",
            "v1": ",".join(["+", "blocking"]),
            "f2": "cf_status_firefox" + central_version,
            "o2": "anyexact",
            "v2": value,
        }
        return params

    def get_autofix_change(self):
        return {
            "comment": {
                "body": "Changing the priority to P2 as the bug is tracked by a release manager for the current nightly.\nSee [Triage for Bugzilla](https://firefox-source-docs.mozilla.org/bug-mgmt/policies/triage-bugzilla.html#automatic-bug-updates) for more information.\nIf you disagree, please discuss with a release manager."
            },
            "priority": "p2",
        }


if __name__ == "__main__":
    MismatchPrioTrackNightly().run()
