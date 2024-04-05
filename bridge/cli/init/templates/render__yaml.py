template = """services:
  - type: web
    plan: free
    runtime: python
    name: {service_name}
    buildCommand: ./build.sh
    startCommand: ./start.sh
    envVars:
      - key: DATABASE_URL
        fromDatabase:
          name: pg-db
          property: connectionString
      - key: SECRET_KEY
        generateValue: true
      - key: WEB_CONCURRENCY
        value: 4

databases:
  - name: pg-db
    plan: free
    databaseName: {database_name}
    user: {database_user}
"""


def render_yaml_template(
    service_name: str, database_name: str = "", database_user: str = ""
) -> str:
    database_name = database_name or service_name
    database_user = database_user or service_name
    return template.format(
        service_name=service_name,
        database_name=database_name,
        database_user=database_user,
    )