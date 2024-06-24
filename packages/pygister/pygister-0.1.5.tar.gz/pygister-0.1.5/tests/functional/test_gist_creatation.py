import pytest

from gist import Gist

# Sample content for creating a gist
sample_content = "print('Hello, World!')"
gist_options = {
    "description": "A hello world program",
    "public": True,
    "filename": "hello.py",
}


@pytest.fixture(scope="module")
def auth_token():
    """Read the authentication token from the file."""
    token = Gist.auth_token()
    if not token:
        pytest.skip("Authentication token not found, skipping tests.")
    return token


@pytest.fixture
def created_gist(auth_token):
    """Fixture to create a gist and ensure it gets deleted after the test."""
    result = Gist.gist(sample_content, gist_options)
    yield result
    # Ensure the gist is deleted after the test
    try:
        Gist.delete_gist(result["id"])
    except Gist.Error as e:
        print(f"Error deleting gist {result['id']}: {e}")


def test_create_gist(created_gist):
    """Test creating a gist."""
    result = created_gist
    assert "id" in result
    assert result["description"] == gist_options["description"]
    assert result["files"][gist_options["filename"]]["content"] == sample_content


def test_list_gists(auth_token):
    """Test listing all gists."""
    gists = Gist.list_all_gists()
    assert isinstance(gists, list)
    assert len(gists) > 0  # Assuming the user has at least one gist


def test_read_gist(auth_token, created_gist):
    """Test reading a specific gist by ID."""
    gist_id = created_gist["id"]
    content = Gist.read_gist(gist_id)
    assert content is not None
    assert len(content) > 0
