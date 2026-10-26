from playwright.sync_api import Page


class InternalUserAPI:
    """Helper untuk memanggil REST API BSN terkait data User (Setup & Teardown Data Tumbal)."""

    def __init__(self, page: Page, base_url: str):
        self.page = page
        self.base_url = base_url

    def create_tumbal_user(self, payload: dict) -> dict:
        """
        Membuat user tumbal via API untuk isolasi data uji.
        TODO: Isi endpoint dan body request saat API backend sudah diketahui.
        """
        # post_response = self.page.request.post(
        #     f"{self.base_url}/api/v1/users",
        #     data=payload,
        # )
        # assert post_response.ok, f"Gagal seeding user via API: {post_response.text()}"
        # return post_response.json().get("data", {})
        pass

    def delete_tumbal_user(self, user_id: str):
        """
        Menghapus user tumbal via API setelah pengujian selesai.
        TODO: Isi endpoint delete saat API backend sudah diketahui.
        """
        # delete_response = self.page.request.delete(
        #     f"{self.base_url}/api/v1/users/{user_id}"
        # )
        # if delete_response.status != 404:
        #     assert delete_response.ok, f"Gagal hapus user via API: {delete_response.text()}"
        pass
