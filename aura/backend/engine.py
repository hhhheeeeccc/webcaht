import json
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("AuraEngine")

class AuraEngine:
    def __init__(self, neon_project_id, linear_team_id):
        self.neon_project_id = neon_project_id
        self.linear_team_id = linear_team_id

    def check_slow_queries(self, slow_queries):
        """
        Identifies queries that need remediation.
        """
        incidents = []
        for q in slow_queries:
            # Logic: If mean execution time > 500ms, it's an incident
            if q.get("mean_exec_time", 0) > 500:
                incidents.append({
                    "title": f"AUR-SQL: Slow Query Detected",
                    "description": f"Database: {q.get('datname')}\nMean Time: {q['mean_exec_time']:.2f}ms\nSQL: {q.get('query')[:200]}...",
                    "priority": 2  # High priority
                })
        return incidents

    def report_incident(self, incident):
        """
        In a production environment, this would call the Linear API.
        For this prototype, we log the intended action.
        """
        logger.info(f"Reporting to Linear Team {self.linear_team_id}: {incident['title']}")
        return True

    def process(self, slow_queries_data):
        logger.info(f"Processing {len(slow_queries_data)} queries from Neon project {self.neon_project_id}")
        incidents = self.check_slow_queries(slow_queries_data)

        results = []
        for incident in incidents:
            success = self.report_incident(incident)
            results.append({"incident": incident, "reported": success})

        return results

if __name__ == "__main__":
    # Example execution with dummy data
    engine = AuraEngine("rapid-term-04723443", "6bcb7b4d-2ca4-482e-980a-52465bf2d7df")
    sample_data = [
        {"datname": "neondb", "query": "SELECT * FROM large_table JOIN other_table...", "mean_exec_time": 1200.50},
        {"datname": "neondb", "query": "SELECT 1", "mean_exec_time": 0.5}
    ]
    engine.process(sample_data)
