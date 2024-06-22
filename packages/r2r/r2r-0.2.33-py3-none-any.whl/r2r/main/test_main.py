from r2r.main.assembly.builder import R2RAppBuilder


def main():
    builder = R2RAppBuilder(from_config="pgvector")
    r2r_app = builder.build()
    r2r_app.serve(host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()
